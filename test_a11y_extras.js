const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

const regex = /<button data-id="\$\{product.id\}" class="add-extra-btn[^>]*>/;
const match = html.match(regex);
if (match) {
    console.log('Add Extra Btn:', match[0].includes('aria-label') ? '✅ HAS ARIA' : '❌ NO ARIA');
    if (!match[0].includes('aria-label')) {
        console.log(`   ${match[0].substring(0, 100)}...`);
    }
}
