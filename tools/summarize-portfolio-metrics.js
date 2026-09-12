#!/usr/bin/env node
/**
 * 从本地埋点队列 JSON 汇总三张作品集轻量卡。
 *
 * 用法：
 *   node tools/summarize-portfolio-metrics.js path/to/aran_analytics_queue.json
 *
 * 导出队列：微信开发者工具 → Storage → aran_analytics_queue → 复制为 JSON 文件
 * （勿提交含设备细节的原始文件到公开仓；只把汇总数字写进 README）
 */
const fs = require('fs');
const path = require('path');

function loadQueue(file) {
  const raw = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (Array.isArray(raw)) return raw;
  if (raw && Array.isArray(raw.queue)) return raw.queue;
  throw new Error('JSON 应为数组，或 { queue: [] }');
}

function main() {
  const file = process.argv[2];
  if (!file) {
    console.error('用法: node tools/summarize-portfolio-metrics.js <queue.json>');
    process.exit(1);
  }
  const queue = loadQueue(path.resolve(file));
  const summaries = queue.filter((r) => r && r.event === 'session_summary');
  const nSessions = summaries.length;

  let completed = 0;
  let fallbackA = 0;
  const urgePairs = [];

  summaries.forEach((row) => {
    const p = row.props || {};
    if (Number(p.completed) === 1) completed += 1;
    if (Number(p.fallbackEntered) === 1) fallbackA += 1;
    const before = Number(p.urgeBefore);
    const after = Number(p.urgeAfter);
    if (before >= 0 && after >= 0 && Number(p.moodResponded) === 1) {
      urgePairs.push({ before, after, delta: before - after });
    }
  });

  // 若 summary 缺 mood，回退扫 mood_submit（认真拖过）
  if (urgePairs.length === 0) {
    const moods = queue.filter((r) => r && r.event === 'mood_submit');
    const bySession = {};
    moods.forEach((r) => {
      const p = r.props || {};
      if (!p.dragged || p.skipped) return;
      const sid = p.sessionId || '_';
      if (!bySession[sid]) bySession[sid] = {};
      bySession[sid][p.phase] = Number(p.value);
    });
    Object.keys(bySession).forEach((sid) => {
      const pre = bySession[sid].pre;
      const post = bySession[sid].post;
      if (Number.isFinite(pre) && Number.isFinite(post)) {
        urgePairs.push({ before: pre, after: post, delta: pre - post });
      }
    });
  }

  const completionRate = nSessions
    ? Math.round((completed / nSessions) * 1000) / 10
    : null;
  const avgDelta = urgePairs.length
    ? Math.round(
      (urgePairs.reduce((s, x) => s + x.delta, 0) / urgePairs.length) * 10
    ) / 10
    : null;

  const out = {
    n_sessions: nSessions,
    completion_rate_pct: completionRate,
    completed_count: completed,
    urge_pair_n: urgePairs.length,
    urge_avg_delta: avgDelta,
    urge_note: '正数=按完后想挠程度平均下降（仅认真拖过的前后探针）',
    fallback_to_A_count: fallbackA,
  };

  console.log(JSON.stringify(out, null, 2));
  console.log('\n--- README 可粘贴 ---');
  console.log(
    `| 完成率 | ${completionRate == null ? '—' : completionRate + '%'} | n=${nSessions} 局有 session_summary |`
  );
  console.log(
    `| 想挠分数前后变化 | ${avgDelta == null ? '—' : (avgDelta > 0 ? '↓' : avgDelta < 0 ? '↑' : '') + Math.abs(avgDelta) + ' 分'} | n=${urgePairs.length} 对认真拖过的前后探针；正数表示平均下降 |`
  );
  console.log(
    `| 退到轻量 A | ${fallbackA} 次 | 来自 session_summary.fallbackEntered；n=${nSessions} |`
  );
}

main();
