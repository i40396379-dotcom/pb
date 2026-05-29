// ═══════════════════════════════════════════════════════════════════════
// PlayBeat Digital — Shared JavaScript
// ═══════════════════════════════════════════════════════════════════════

// ──────────────────────── STATE MANAGEMENT ──────────────────────────

let currentUser = null;
let wishlist = [];
let orders = [];
let cart = [];

// ──────────────────────── PRODUCT DATA ──────────────────────────

const products = {
  trending: [
    {icon:'🎮',name:'Elden Ring',cat:'Action RPG',price:'$39.99',old:'$59.99',stars:5,badge:'hot'},
    {icon:'⚡',name:'ChatGPT Plus (1M)',cat:'AI Assistant',price:'$20',old:'$30',stars:5,badge:'hot'},
    {icon:'🎁',name:'PlayStation Network $50',cat:'Gift Card',price:'$45',old:'$50',stars:5,badge:''},
    {icon:'🖼️',name:'Midjourney Basic (1M)',cat:'AI Image',price:'$10',old:'$15',stars:5,badge:'sale'},
    {icon:'💿',name:'Windows 11 Pro',cat:'OS License',price:'$19',old:'$199',stars:5,badge:'sale'},
    {icon:'🎮',name:'Call of Duty Modern Warfare III',cat:'Shooter',price:'$59.99',old:'$69.99',stars:4,badge:''},
    {icon:'🤖',name:'Claude Pro (1M)',cat:'AI Assistant',price:'$20',old:'$30',stars:5,badge:''},
    {icon:'🎧',name:'Spotify Premium (1M)',cat:'Music',price:'$8.99',old:'$11.99',stars:5,badge:''},
  ],
  bestvalue: [
    {icon:'🎮',name:'Indie Bundle x10',cat:'Game Bundle',price:'$29.99',old:'$89.99',stars:5,badge:'sale'},
    {icon:'🤖',name:'AI Mega Bundle (3 tools)',cat:'Bundle',price:'$39.99',old:'$79.99',stars:5,badge:'sale'},
    {icon:'💿',name:'Microsoft Office 365 (1yr)',cat:'Productivity',price:'$29',old:'$99',stars:5,badge:'sale'},
    {icon:'🔒',name:'ExpressVPN (1yr)',cat:'VPN',price:'$29.99',old:'$119.95',stars:5,badge:''},
    {icon:'🎁',name:'Amazon Gift Card $100',cat:'Gift Card',price:'$95',old:'$100',stars:5,badge:''},
    {icon:'🎮',name:'Xbox Game Pass (3M)',cat:'Subscription',price:'$19.99',old:'$44.97',stars:5,badge:'hot'},
  ],
  games: [
    {icon:'🏆',name:'The Blackened Realm',cat:'Action RPG',price:'$59.99',old:'$69.99',stars:5,badge:'hot'},
    {icon:'🚀',name:'Stellar Command',cat:'Space Strategy',price:'$29.99',old:'$39.99',stars:5,badge:''},
    {icon:'⚽',name:'EA Sports FC 25',cat:'Sports',price:'$59.99',old:'$69.99',stars:4,badge:''},
    {icon:'🎮',name:'Final Fantasy XVI',cat:'RPG',price:'$49.99',old:'$59.99',stars:5,badge:''},
    {icon:'🧩',name:'Portal 3',cat:'Puzzle',price:'$39.99',old:'$49.99',stars:5,badge:''},
    {icon:'🏃',name:'Cyberpunk 2077 Ultimate',cat:'Action',price:'$49.99',old:'$79.99',stars:5,badge:'sale'},
    {icon:'🌍',name:'GTA VI',cat:'Action',price:'$79.99',old:'$89.99',stars:5,badge:'hot'},
    {icon:'🎯',name:'Baldur\'s Gate 4',cat:'RPG',price:'$69.99',old:'$79.99',stars:5,badge:''},
  ],
  giftcards: [
    {icon:'🎮',name:'PlayStation Store $50',cat:'PlayStation',price:'$45',old:'$50',stars:5,badge:''},
    {icon:'🎮',name:'Xbox Game Pass $29',cat:'Xbox',price:'$25',old:'$29',stars:5,badge:''},
    {icon:'🎮',name:'Steam Wallet $100',cat:'Steam',price:'$95',old:'$100',stars:5,badge:''},
    {icon:'🎵',name:'Google Play $50',cat:'Google Play',price:'$45',old:'$50',stars:5,badge:''},
    {icon:'🍎',name:'Apple Gift Card $100',cat:'Apple',price:'$92',old:'$100',stars:5,badge:'sale'},
    {icon:'📱',name:'Amazon Gift Card $50',cat:'Amazon',price:'$48',old:'$50',stars:5,badge:''},
    {icon:'🎮',name:'Nintendo eShop $50',cat:'Nintendo',price:'$45',old:'$50',stars:5,badge:''},
    {icon:'🌐',name:'Roblox 10000 Robux',cat:'Roblox',price:'$89',old:'$100',stars:5,badge:''},
  ],
  softwares: [
    {icon:'💻',name:'Windows 11 Pro',cat:'OS License',price:'$19',old:'$199',stars:5,badge:'sale'},
    {icon:'🎨',name:'Adobe Photoshop CC',cat:'Design',price:'$19.99',old:'$54.99',stars:5,badge:''},
    {icon:'🛡️',name:'Norton 360 (1yr)',cat:'Security',price:'$34.99',old:'$99.99',stars:5,badge:'sale'},
    {icon:'📊',name:'Microsoft Office 365',cat:'Productivity',price:'$29',old:'$99',stars:5,badge:'sale'},
    {icon:'🔒',name:'Bitdefender Total Security',cat:'Security',price:'$24.99',old:'$79.99',stars:5,badge:'sale'},
    {icon:'💾',name:'WinRAR Lifetime',cat:'Utility',price:'$25',old:'$29',stars:5,badge:''},
    {icon:'🔐',name:'ExpressVPN (1yr)',cat:'VPN',price:'$29.99',old:'$119.95',stars:5,badge:'sale'},
    {icon:'✏️',name:'Grammarly Premium',cat:'Productivity',price:'$59',old:'$119',stars:5,badge:''},
  ],
  aitools: [
    {icon:'🤖',name:'ChatGPT Plus (1M)',cat:'AI Assistant',price:'$20',old:'$30',stars:5,badge:'hot'},
    {icon:'🖼️',name:'Midjourney Subscription',cat:'AI Image',price:'$10',old:'$15',stars:5,badge:''},
    {icon:'🤖',name:'Claude Pro (1M)',cat:'AI Assistant',price:'$20',old:'$30',stars:5,badge:''},
    {icon:'📹',name:'RunwayML Pro',cat:'AI Video',price:'$15.99',old:'$28',stars:5,badge:''},
    {icon:'🎵',name:'Murf Studio Voice AI',cat:'AI Voice',price:'$9.99',old:'$19.99',stars:5,badge:''},
    {icon:'🔍',name:'Perplexity Pro',cat:'AI Search',price:'$20',old:'$30',stars:5,badge:''},
    {icon:'✍️',name:'Jasper AI Starter',cat:'AI Assistant',price:'$39',old:'$125',stars:5,badge:'sale'},
    {icon:'🎨',name:'Adobe Firefly (1M)',cat:'AI Image',price:'$4.99',old:'$9.99',stars:5,badge:''},
  ],
  gameitems: [
    {icon:'🐉',name:'CS2 Dragon Lore AWP',cat:'Weapon Skin',price:'$299',old:'$500',stars:5,badge:'hot'},
    {icon:'👕',name:'Valorant Prestige Bundle',cat:'Bundle',price:'$79.99',old:'$99.99',stars:5,badge:''},
    {icon:'⚔️',name:'Fortnite Superhero Skin',cat:'Skin',price:'$19.99',old:'$24.99',stars:5,badge:''},
    {icon:'💰',name:'PUBG 50000 UC',cat:'Currency',price:'$249',old:'$350',stars:5,badge:''},
    {icon:'🎭',name:'League of Legends Prestige Skin',cat:'Skin',price:'$29.99',old:'$39.99',stars:5,badge:''},
    {icon:'😂',name:'Dota 2 Arcana Bundle',cat:'Bundle',price:'$49.99',old:'$69.99',stars:5,badge:'sale'},
    {icon:'🎪',name:'Apex Legends Battle Pass',cat:'Pass',price:'$9.99',old:'$14.99',stars:5,badge:''},
    {icon:'🏹',name:'Overwatch 2 Premium Skin',cat:'Skin',price:'$19.99',old:'$24.99',stars:5,badge:''},
  ],
  accounts: [
    {icon:'📺',name:'Netflix Premium 4K',cat:'Streaming',price:'$14.99',old:'$19.99',stars:5,badge:''},
    {icon:'🎵',name:'Spotify Premium Lifetime',cat:'Music',price:'$99',old:'$299',stars:5,badge:'sale'},
    {icon:'🎨',name:'Adobe Creative Cloud',cat:'Design',price:'$39.99',old:'$59.99',stars:5,badge:''},
    {icon:'📚',name:'Skillshare Premium',cat:'Education',price:'$29',old:'$39',stars:5,badge:''},
    {icon:'✍️',name:'Medium Membership',cat:'Writing',price:'$5',old:'$15/mo',stars:5,badge:''},
    {icon:'🎓',name:'Coursera Plus',cat:'Education',price:'$199/yr',old:'$399/yr',stars:5,badge:'sale'},
  ],
  subs: [
    {icon:'🎮',name:'Xbox Game Pass Ultimate',cat:'Gaming',price:'$16.99',old:'$19.99',stars:5,badge:''},
    {icon:'🎮',name:'PlayStation Plus Extra',cat:'Gaming',price:'$14.99',old:'$17.99',stars:5,badge:''},
    {icon:'🎨',name:'Adobe Creative Cloud',cat:'Creative',price:'$54.99',old:'$82.49',stars:5,badge:'sale'},
    {icon:'📺',name:'Disney+ Bundle',cat:'Streaming',price:'$13.99',old:'$24.99',stars:5,badge:''},
    {icon:'🔒',name:'1Password Family',cat:'Security',price:'$4.99',old:'$9.99',stars:5,badge:'sale'},
    {icon:'📚',name:'Kindle Unlimited',cat:'Productivity',price:'$11.99',old:'$14.99',stars:5,badge:''},
  ],
  topupPlatforms: [
    {name:'Steam',icon:'🎮',hint:'Steam Wallet Funds'},
    {name:'PlayStation',icon:'🎮',hint:'PS Network Credits'},
    {name:'Xbox',icon:'🎮',hint:'Microsoft Balance'},
    {name:'PUBG Mobile',icon:'📱',hint:'UC Top Up'},
    {name:'Free Fire',icon:'🔥',hint:'Diamond Recharge'},
    {name:'Fortnite',icon:'⚡',hint:'V-Bucks'},
  ],
};

// ──────────────────────── MODAL FUNCTIONS ──────────────────────────

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

function switchModal(closeId, openId) {
  closeModal(closeId);
  setTimeout(() => openModal(openId), 200);
}

// ──────────────────────── AUTH FUNCTIONS ──────────────────────────

function doSignIn() {
  const email = document.getElementById('siEmail')?.value.trim();
  const pass = document.getElementById('siPass')?.value.trim();
  const error = document.getElementById('siError');
  const success = document.getElementById('signinSuccess');

  if (!email || !pass) {
    if (error) error.style.display = 'block';
    return;
  }

  if (error) error.style.display = 'none';
  if (success) success.style.display = 'block';

  currentUser = {
    email,
    first: email.split('@')[0],
    last: 'Member',
    isPrime: true,
  };

  updateHeaderUser();
  
  setTimeout(() => {
    closeModal('signinModal');
    if (success) success.style.display = 'none';
  }, 1500);
}

function doSignUp() {
  const first = document.getElementById('suFirst')?.value.trim();
  const last = document.getElementById('suLast')?.value.trim();
  const email = document.getElementById('suEmail')?.value.trim();
  const pass = document.getElementById('suPass')?.value.trim();
  const terms = document.getElementById('suTerms')?.checked;
  const error = document.getElementById('suError');
  const success = document.getElementById('signupSuccess');

  if (!first || !last || !email || !pass || !terms) {
    if (error) error.style.display = 'block';
    return;
  }

  if (error) error.style.display = 'none';
  if (success) success.style.display = 'block';

  currentUser = { email, first, last, isPrime: true };
  updateHeaderUser();

  setTimeout(() => {
    closeModal('signupModal');
    if (success) success.style.display = 'none';
  }, 1500);
}

function doLogout() {
  currentUser = null;
  wishlist = [];
  orders = [];
  cart = [];
  updateHeaderUser();
  window.location.href = 'index.html';
}

function updateHeaderUser() {
  const guest = document.getElementById('headerGuest');
  const user = document.getElementById('headerUser');
  const headerName = document.getElementById('headerName');

  if (guest && user) {
    if (currentUser) {
      guest.style.display = 'none';
      user.style.display = 'flex';
      if (headerName) headerName.textContent = currentUser.first;
    } else {
      guest.style.display = 'flex';
      user.style.display = 'none';
    }
  }
}

// ──────────────────────── PRODUCT FUNCTIONS ──────────────────────────

function renderGrid(gridId, items) {
  const grid = document.getElementById(gridId);
  if (!grid) return;

  grid.innerHTML = items.map(p => `
    <div class="product-card">
      <div class="product-image">
        <span>${p.icon}</span>
        ${p.badge ? `<div class="product-badge badge-${p.badge}">${p.badge.toUpperCase()}</div>` : ''}
        <button class="wishlist-btn" onclick="toggleWishlist('${p.name}');event.stopPropagation()">♡</button>
      </div>
      <div class="product-body">
        <div class="product-cat">${p.cat}</div>
        <div class="product-name">${p.name}</div>
        <div class="product-stars">${'★'.repeat(p.stars)}${'☆'.repeat(5-p.stars)}</div>
        <div class="product-footer">
          <div class="product-price">
            <span class="main">${p.price}</span>
            ${p.old ? `<span class="old">${p.old}</span>` : ''}
          </div>
          <button class="btn-buy" onclick='openCheckout(${JSON.stringify(p).replace(/'/g, "&apos;")})'>Buy</button>
        </div>
      </div>
    </div>
  `).join('');
}

// ──────────────────────── CART & CHECKOUT ──────────────────────────

function openCheckout(product) {
  if (!currentUser) {
    openModal('signinModal');
    return;
  }

  document.getElementById('coIcon').textContent = product.icon || '📦';
  document.getElementById('coName').textContent = product.name || 'Product';
  document.getElementById('coCat').textContent = product.cat || 'Digital Item';
  document.getElementById('coPrice').textContent = product.price || '$0';
  document.getElementById('coTotal').textContent = product.price || '$0';

  openModal('checkoutModal');
}

function selectPay(el) {
  document.querySelectorAll('.pay-method').forEach(m => m.classList.remove('selected'));
  el.classList.add('selected');
  const cardFields = document.getElementById('cardFields');
  if (cardFields) {
    cardFields.style.display = el.textContent.includes('💳') ? 'block' : 'none';
  }
}

function doCheckout() {
  if (!currentUser) return;

  const cardFields = document.getElementById('cardFields');
  if (cardFields && cardFields.style.display !== 'none') {
    const card = document.getElementById('coCard')?.value.trim();
    const exp = document.getElementById('coExp')?.value.trim();
    const cvv = document.getElementById('coCvv')?.value.trim();
    if (!card || !exp || !cvv) {
      const error = document.getElementById('coError');
      if (error) error.style.display = 'block';
      return;
    }
  }

  const form = document.getElementById('checkoutForm');
  const success = document.getElementById('checkoutSuccess');
  const key = 'XXXX-' + Math.random().toString(36).substr(2, 9).toUpperCase() + '-XXXX';

  if (form && success) {
    form.style.display = 'none';
    success.style.display = 'block';
    document.getElementById('deliveryKey').textContent = key;

    const price = document.getElementById('coTotal').textContent;
    orders.push({
      name: document.getElementById('coName').textContent,
      icon: document.getElementById('coIcon').textContent,
      price,
      status: 'Delivered',
      date: new Date().toLocaleDateString(),
    });
  }
}

function formatCardNumber(input) {
  input.value = input.value.replace(/\s/g, '').replace(/(.{4})/g, '$1 ').trim();
}

// ──────────────────────── WISHLIST ──────────────────────────────

function toggleWishlist(productName) {
  const idx = wishlist.findIndex(p => p.name === productName);
  if (idx > -1) {
    wishlist.splice(idx, 1);
  } else {
    const product = Object.values(products).flat().find(p => p.name === productName);
    if (product) wishlist.push(product);
  }
  updateWishlistCount();
}

function updateWishlistCount() {
  const counts = document.querySelectorAll('.wish-count');
  counts.forEach(c => {
    if (wishlist.length > 0) {
      c.textContent = wishlist.length;
      c.style.display = 'inline-flex';
    } else {
      c.style.display = 'none';
    }
  });
}

// ──────────────────────── SEARCH ──────────────────────────────

function doSearch() {
  const input = document.getElementById('searchInput');
  const category = document.getElementById('searchCat');
  const dropdown = document.getElementById('searchDropdown');

  if (!input || !dropdown) return;

  const query = input.value.toLowerCase().trim();
  const cat = category?.value || 'all';

  if (!query) {
    dropdown.innerHTML = '';
    dropdown.style.display = 'none';
    return;
  }

  let results = [];
  Object.entries(products).forEach(([key, items]) => {
    if (Array.isArray(items)) {
      results = results.concat(items.filter(p =>
        p.name.toLowerCase().includes(query) &&
        (cat === 'all' || key.toLowerCase().includes(cat.toLowerCase()))
      ));
    }
  });

  results = results.slice(0, 8);

  if (results.length > 0) {
    dropdown.innerHTML = results.map(p => `
      <div class="search-result" onclick='openCheckout(${JSON.stringify(p).replace(/'/g, "&apos;")}); document.getElementById("searchDropdown").style.display="none"'>
        <span class="search-icon">${p.icon}</span>
        <div>
          <div class="search-name">${p.name}</div>
          <div class="search-cat">${p.cat}</div>
        </div>
        <div class="search-price">${p.price}</div>
      </div>
    `).join('');
    dropdown.style.display = 'block';
  } else {
    dropdown.innerHTML = '<div style="padding:12px;color:#555;text-align:center">No results found</div>';
    dropdown.style.display = 'block';
  }
}

// ──────────────────────── TAB SWITCHING ──────────────────────────────

function switchTab(btn, tabId) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  const tab = document.getElementById(tabId);
  if (tab) tab.classList.add('active');
}

function switchAcctTab(btn, tabId) {
  document.querySelectorAll('.acct-tab').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.acct-panel').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  const panel = document.getElementById(tabId);
  if (panel) panel.classList.add('active');
}

// ──────────────────────── PROFILE ──────────────────────────────

function saveProfile() {
  const first = document.getElementById('profileFirst')?.value.trim();
  const last = document.getElementById('profileLast')?.value.trim();
  const email = document.getElementById('profileEmail')?.value.trim();

  if (currentUser) {
    currentUser.first = first || currentUser.first;
    currentUser.last = last || currentUser.last;
    currentUser.email = email || currentUser.email;
    updateHeaderUser();
    alert('Profile updated successfully!');
  }
}

// ──────────────────────── INIT ──────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  updateHeaderUser();
  updateWishlistCount();

  // Close modals on overlay click
  document.querySelectorAll('.modal-overlay').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal(modal.id);
      }
    });
  });

  // Close search dropdown on outside click
  document.addEventListener('click', (e) => {
    const dropdown = document.getElementById('searchDropdown');
    const searchBar = document.querySelector('.search-bar');
    if (dropdown && !searchBar?.contains(e.target)) {
      dropdown.style.display = 'none';
    }
  });
});
