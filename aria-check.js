const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const regex = /<button[^>]*>[\s\S]*?<\/button>/gi;
let match;
let count = 0;
while ((match = regex.exec(html)) !== null) {
  const btnHtml = match[0];
  if (!btnHtml.toLowerCase().includes('aria-label') && (
    btnHtml.includes('<svg') ||
    btnHtml.includes('&times;') ||
    btnHtml.match(/>(\s*)[+\-x✖✕](\s*)<\/button>/i)
  )) {
    console.log(`Button missing aria-label: ${btnHtml.substring(0, 100)}...`);
    count++;
  }
}
console.log(`Found ${count} buttons missing aria-label.`);
