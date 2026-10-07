// node render.cjs [contact|video]  — frames are pure function of t via window.seek(t)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const mode = process.argv[2] || 'video';
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + path.join(__dirname, 'index.html'));
  await p.evaluate(() => window.ready);
  if (mode === 'contact') {
    const times = JSON.parse(process.argv[3]);
    for (const [i, t] of times.entries()) { await p.evaluate(t => seek(t), t); await p.screenshot({ path: `contact/f${String(i).padStart(2, '0')}.png` }); }
  } else {
    const fps = 30, dur = 60, N = fps * dur;
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'medium', 'silent.mp4'], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let f = 0; f < N; f++) {
      await p.evaluate(t => seek(t), f / fps);
      const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 300 === 0) console.log('frame', f);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  console.log('errors', errs); await b.close();
})();
