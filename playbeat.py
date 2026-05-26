#!/usr/bin/env python3
"""
PlayBeat Digital — Site Generator v2
Builds all 15 HTML pages from shared template + per-page content.

Usage:
    python3 build_site.py

Output:
    ./dist/           — 15 HTML files
    ./dist/shared.css — shared stylesheet
    ./dist/shared.js  — shared JavaScript

Then open dist/index.html in a browser.
"""

import os, shutil
from pathlib import Path

OUT = Path("dist")
OUT.mkdir(exist_ok=True)

# Copy shared assets (must exist alongside this script)
for f in ("shared.css", "shared.js"):
    src = Path(f)
    if src.exists():
        shutil.copy(src, OUT / f)
    else:
        print(f"  ⚠  WARNING: {f} not found — copy it next to this script")

# ─── SHARED FRAGMENTS ──────────────────────────────────────────

TICKER = '''<div class="ticker-bar">
  <div class="ticker-inner">
    <span>🔥 Valorant Elderflame Bundle — $89</span>
    <span>⚡ ChatGPT Plus 1M — $20</span>
    <span>🎮 PS Plus 12M — $59</span>
    <span>💎 Adobe CC All Apps — $54</span>
    <span>🤖 Midjourney Basic — $10</span>
    <span>🆓 Free Gift Card on Orders $50+</span>
    <span>🔒 SSL Secured · Instant Delivery</span>
    <span>🔥 Valorant Elderflame Bundle — $89</span>
    <span>⚡ ChatGPT Plus 1M — $20</span>
    <span>🎮 PS Plus 12M — $59</span>
    <span>💎 Adobe CC All Apps — $54</span>
    <span>🤖 Midjourney Basic — $10</span>
    <span>🆓 Free Gift Card on Orders $50+</span>
    <span>🔒 SSL Secured · Instant Delivery</span>
  </div>
</div>'''

HEADER = '''<header>
  <div class="header-top">
    <div class="header-top-inner">
      <div class="search-wrap">
        <div class="search-bar">
          <div class="search-bar-bg"></div>
          <select class="search-category" id="searchCat" onchange="doSearch()">
            <option value="all">All</option>
            <option value="games">Games</option>
            <option value="ai">AI Tools</option>
            <option value="software">Software</option>
            <option value="giftcards">Gift Cards</option>
            <option value="subs">Subscriptions</option>
            <option value="topup">Top Up</option>
            <option value="items">Game Items</option>
            <option value="accounts">Accounts</option>
          </select>
          <input class="search-input" id="searchInput" type="text"
            placeholder="Search games, AI tools, subscriptions…"
            oninput="doSearch()" autocomplete="off">
          <button class="search-btn" onclick="doSearch()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
            </svg>
          </button>
        </div>
        <div class="search-dropdown" id="searchDropdown"></div>
      </div>
    </div>
  </div>
  <div class="header-inner">
    <a class="logo" href="index.html">
      <div class="logo-icon">▶</div>
      <div class="logo-text">Play<span>Beat</span></div>
    </a>
    <nav>
      <a href="index.html"          class="nav-item">Home</a>
      <a href="games.html"          class="nav-item">Games</a>
      <a href="gift-cards.html"     class="nav-item">Gift Cards</a>
      <a href="software.html"       class="nav-item">Software</a>
      <a href="ai-tools.html"       class="nav-item">AI Tools</a>
      <a href="game-items.html"     class="nav-item">Game Items</a>
      <a href="accounts.html"       class="nav-item">Accounts</a>
      <a href="subscriptions.html"  class="nav-item">Subscriptions</a>
      <a href="top-up.html"         class="nav-item">Top Up</a>
      <a href="trending.html"       class="nav-item nav-special">🔥 Trending</a>
      <a href="best-value.html"     class="nav-item nav-special">💎 Best Value</a>
    </nav>
    <div class="header-actions">
      <div id="headerGuest" style="display:flex;align-items:center;gap:12px">
        <button class="btn-wishlist-icon" onclick="window.location.href='my-account.html'">
          ♡ <span class="wish-count" id="wishlistCount" style="display:none">0</span>
        </button>
        <button class="btn-login" onclick="openModal('signinModal')">Sign In</button>
        <button class="btn-prime" onclick="openModal('signupModal')">Join Prime</button>
      </div>
      <div id="headerUser" style="display:none;align-items:center;gap:12px">
        <button class="btn-wishlist-icon" onclick="window.location.href='my-account.html'">
          ♡ <span class="wish-count" id="wishlistCount2" style="display:none">0</span>
        </button>
        <div class="user-chip" onclick="window.location.href='my-account.html'">
          <span class="user-chip-avatar">👤</span>
          <span id="headerName">User</span>
        </div>
      </div>
    </div>
  </div>
</header>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="index.html" style="margin-bottom:0;display:inline-flex">
          <div class="logo-icon">▶</div>
          <div class="logo-text">Play<span>Beat</span></div>
        </a>
        <p>The premier destination for digital products. Games, AI tools, subscriptions,
           gift cards &amp; more — delivered instantly, globally.</p>
      </div>
      <div class="footer-col">
        <h4>Marketplace</h4>
        <ul>
          <li><a href="games.html">Games</a></li>
          <li><a href="ai-tools.html">AI Tools</a></li>
          <li><a href="software.html">Software</a></li>
          <li><a href="gift-cards.html">Gift Cards</a></li>
          <li><a href="subscriptions.html">Subscriptions</a></li>
          <li><a href="game-items.html">Game Items</a></li>
          <li><a href="accounts.html">Accounts</a></li>
          <li><a href="top-up.html">Top Up</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Discover</h4>
        <ul>
          <li><a href="trending.html">🔥 Trending</a></li>
          <li><a href="best-value.html">💎 Best Value</a></li>
          <li><a href="outsource.html">Outsource</a></li>
          <li><a href="our-team.html">Our Team</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
          <li><a href="refund.html">Refund Policy</a></li>
          <li><a href="my-account.html">My Account</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 <span>PlayBeat Digital</span>. All rights reserved.</span>
      <span>Built for prime members worldwide ⭐</span>
    </div>
  </div>
</footer>'''

MODALS = '''<!-- ===== SIGN IN MODAL ===== -->
<div class="modal-overlay" id="signinModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('signinModal')">✕</button>
    <div class="modal-logo">Play<span>Beat</span></div>
    <div class="modal-sub">Prime Digital Marketplace</div>
    <div class="modal-title">Sign In</div>
    <div class="modal-success" id="signinSuccess">✓ Signed in successfully!</div>
    <button class="btn-social">🔵 Continue with Google</button>
    <button class="btn-social">🐙 Continue with GitHub</button>
    <div class="modal-divider">or use email</div>
    <div class="form-group">
      <label class="form-label">Email</label>
      <input class="form-input" id="siEmail" type="email" placeholder="you@email.com">
    </div>
    <div class="form-group">
      <label class="form-label">Password</label>
      <input class="form-input" id="siPass" type="password" placeholder="••••••••">
    </div>
    <div class="modal-error" id="siError">Invalid email or password.</div>
    <div style="text-align:right;margin-bottom:20px">
      <a style="color:var(--gold);font-size:12px;cursor:pointer;font-family:'Share Tech Mono',monospace">Forgot password?</a>
    </div>
    <button class="btn-hero-primary" style="width:100%;padding:13px;border-radius:4px" onclick="doSignIn()">Sign In →</button>
    <div class="modal-switch">Don't have an account? <a onclick="switchModal('signinModal','signupModal')">Create one free</a></div>
  </div>
</div>

<!-- ===== SIGN UP MODAL ===== -->
<div class="modal-overlay" id="signupModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('signupModal')">✕</button>
    <div class="modal-logo">Play<span>Beat</span></div>
    <div class="modal-sub">Prime Digital Marketplace</div>
    <div class="modal-title">Create Account</div>
    <div class="modal-success" id="signupSuccess">✓ Account created! Welcome aboard.</div>
    <button class="btn-social">🔵 Continue with Google</button>
    <button class="btn-social">🐙 Continue with GitHub</button>
    <div class="modal-divider">or use email</div>
    <div class="form-row">
      <div class="form-group"><label class="form-label">First Name</label><input class="form-input" id="suFirst" type="text" placeholder="Alex"></div>
      <div class="form-group"><label class="form-label">Last Name</label><input class="form-input" id="suLast" type="text" placeholder="Carter"></div>
    </div>
    <div class="form-group"><label class="form-label">Email</label><input class="form-input" id="suEmail" type="email" placeholder="you@email.com"></div>
    <div class="form-group"><label class="form-label">Password</label><input class="form-input" id="suPass" type="password" placeholder="Min. 6 characters"></div>
    <div class="modal-error" id="suError">Please fill all fields correctly.</div>
    <div class="checkbox-row">
      <input type="checkbox" id="suTerms">
      <label for="suTerms">I agree to the <a href="terms.html">Terms of Service</a> and <a href="privacy.html">Privacy Policy</a></label>
    </div>
    <button class="btn-hero-primary" style="width:100%;padding:13px;border-radius:4px" onclick="doSignUp()">Create Account →</button>
    <div class="modal-switch">Already have an account? <a onclick="switchModal('signupModal','signinModal')">Sign in</a></div>
  </div>
</div>

<!-- ===== CHECKOUT MODAL ===== -->
<div class="modal-overlay" id="checkoutModal">
  <div class="modal-box" style="max-width:680px">
    <button class="modal-close" onclick="closeModal('checkoutModal')">✕</button>
    <div class="modal-title" id="checkoutTitle">Checkout</div>
    <div style="font-family:'Share Tech Mono',monospace;font-size:11px;color:#555;margin-bottom:24px;letter-spacing:2px">SECURE PAYMENT · INSTANT DELIVERY</div>
    <div id="checkoutForm">
      <div class="checkout-grid">
        <div>
          <div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:#555;letter-spacing:2px;margin-bottom:14px">ORDER SUMMARY</div>
          <div class="checkout-summary">
            <div class="checkout-item">
              <div class="checkout-item-icon" id="coIcon">🎮</div>
              <div>
                <div class="checkout-item-name" id="coName">Product</div>
                <div class="checkout-item-cat"  id="coCat">Category</div>
              </div>
              <div class="checkout-item-price" id="coPrice">$0</div>
            </div>
            <div class="checkout-total">
              <div><div class="checkout-total-label">Total</div></div>
              <div class="checkout-total-price" id="coTotal">$0</div>
            </div>
          </div>
        </div>
        <div>
          <div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:#555;letter-spacing:2px;margin-bottom:14px">PAYMENT METHOD</div>
          <div class="payment-methods">
            <div class="pay-method selected" onclick="selectPay(this)">💳 Card</div>
            <div class="pay-method" onclick="selectPay(this)">🅿️ PayPal</div>
            <div class="pay-method" onclick="selectPay(this)">₿ Crypto</div>
            <div class="pay-method" onclick="selectPay(this)">🍎 Apple Pay</div>
          </div>
          <div id="cardFields">
            <div class="form-group"><label class="form-label">Card Number</label><input class="form-input" id="coCard" type="text" placeholder="1234 5678 9012 3456" maxlength="19" oninput="formatCard(this)"></div>
            <div class="form-row">
              <div class="form-group"><label class="form-label">Expiry</label><input class="form-input" id="coExp" type="text" placeholder="MM/YY" maxlength="5"></div>
              <div class="form-group"><label class="form-label">CVV</label><input class="form-input" id="coCvv" type="password" placeholder="•••" maxlength="4"></div>
            </div>
            <div class="form-group"><label class="form-label">Name on Card</label><input class="form-input" id="coCardName" type="text" placeholder="Alex Carter"></div>
          </div>
          <div class="modal-error" id="coError" style="margin-top:-4px">Please complete all card details.</div>
          <button class="btn-hero-primary" style="width:100%;padding:14px;border-radius:4px;margin-top:8px" onclick="doCheckout()">🔒 Pay &amp; Get Instant Delivery</button>
          <div style="text-align:center;font-size:11px;color:#333;font-family:'Share Tech Mono',monospace;margin-top:10px;letter-spacing:1px">256-bit SSL · Verified Secure</div>
        </div>
      </div>
    </div>
    <div class="checkout-success" id="checkoutSuccess">
      <div class="big-icon">🎉</div>
      <h3>Order Complete!</h3>
      <p>Your digital product has been delivered instantly.</p>
      <div class="key-box" id="deliveryKey">XXXX-XXXX-XXXX-XXXX</div>
      <p style="font-size:12px;color:#444;font-family:'Share Tech Mono',monospace">Save this key · Check email for full details</p>
      <button class="btn-hero-primary" style="margin-top:20px;padding:12px 32px;border-radius:4px"
        onclick="closeModal('checkoutModal');window.location.href='my-account.html'">View My Orders</button>
    </div>
  </div>
</div>'''

# ─── PAGE TEMPLATE ──────────────────────────────────────────────

def page(title, body, extra_js="", extra_css=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — PlayBeat Digital</title>
<link rel="stylesheet" href="shared.css">
{extra_css}
</head>
<body>

{TICKER}
{HEADER}

<main>
{body}
</main>

{FOOTER}
{MODALS}

<script src="shared.js"></script>
{extra_js}
</body>
</html>
'''

# ─── REUSABLE FRAGMENTS ──────────────────────────────────────────

TRUST = '''<div class="trust-strip">
  <div class="trust-item"><span class="icon">⚡</span><div><strong>Instant Delivery</strong><span>Keys sent in seconds</span></div></div>
  <div class="trust-item"><span class="icon">🔒</span><div><strong>256-bit SSL</strong><span>Bank-grade security</span></div></div>
  <div class="trust-item"><span class="icon">✅</span><div><strong>Verified Products</strong><span>100% authentic keys</span></div></div>
  <div class="trust-item"><span class="icon">🌍</span><div><strong>Global Access</strong><span>Available in 100+ countries</span></div></div>
  <div class="trust-item"><span class="icon">💬</span><div><strong>24/7 Support</strong><span>Real humans, always on</span></div></div>
</div>'''

# ─── PAGES ──────────────────────────────────────────────────────

pages = {}

# ── 1. INDEX (Home) ─────────────────────────────────────────────
pages["index.html"] = page("Home", f'''
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-content">
    <div>
      <div class="hero-badge"><div class="badge-dot"></div> Prime Exclusive Marketplace</div>
      <h1 class="hero-title">
        The Future<br>
        <span class="line-gold">Of Digital</span><br>
        <span class="line-silver">Commerce</span>
      </h1>
      <p class="hero-desc">
        Games, AI tools, gift cards, subscriptions &amp; more.
        <strong>Instant delivery. Global reach. Prime quality.</strong>
      </p>
      <div class="hero-cta">
        <a href="trending.html" class="btn-hero-primary">🔥 Shop Trending</a>
        <a href="best-value.html" class="btn-hero-secondary">💎 Best Value</a>
      </div>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">500K+</div><div class="stat-label">Products Sold</div></div>
        <div class="stat-item"><div class="stat-num">120+</div><div class="stat-label">Categories</div></div>
        <div class="stat-item"><div class="stat-num">4.9★</div><div class="stat-label">Avg Rating</div></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-hex-grid" id="heroHexGrid"></div>
    </div>
  </div>
</section>

<div class="main">
  <div class="brands-row">
    <div class="brands-inner" id="brandsMarquee"></div>
  </div>

  <section class="section">
    <div class="section-header">
      <div>
        <div class="section-title">🔥 <span>Trending</span> Now</div>
        <div class="section-sub">Most purchased this week</div>
      </div>
      <a href="trending.html" class="btn-viewall">View All →</a>
    </div>
    <div class="product-grid" id="trendingGrid"></div>
  </section>

  <div class="promo-banner">
    <div>
      <div class="promo-tag">Prime Exclusive</div>
      <div class="promo-title">AI TOOLS <span>MEGA BUNDLE</span></div>
      <div class="promo-sub">5 AI subscriptions for the price of 2 — Limited time offer</div>
    </div>
    <a href="ai-tools.html" class="btn-hero-primary">Grab Bundle →</a>
  </div>

  <section class="section">
    <div class="section-header">
      <div>
        <div class="section-title">Browse <span>Categories</span></div>
        <div class="section-sub">Everything digital in one place</div>
      </div>
    </div>
    <div class="cat-grid" id="catGrid"></div>
  </section>

  <section class="section">
    <div class="section-header">
      <div>
        <div class="section-title">💎 <span>Best Value</span></div>
        <div class="section-sub">Maximum quality, minimum spend</div>
      </div>
      <a href="best-value.html" class="btn-viewall">View All →</a>
    </div>
    <div class="product-grid" id="bestValueGrid"></div>
  </section>

  {TRUST}
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => {
  renderGrid('trendingGrid', products.trending.slice(0,8));
  renderGrid('bestValueGrid', products.bestvalue.slice(0,6));
  const cats = [
    {icon:'🎮', name:'Games',         from:'From $4.99',  href:'games.html',         badge:'hot'},
    {icon:'🤖', name:'AI Tools',      from:'From $9.99',  href:'ai-tools.html',      badge:'hot'},
    {icon:'📋', name:'Subscriptions', from:'From $7.99',  href:'subscriptions.html', badge:''},
    {icon:'🎁', name:'Gift Cards',    from:'From $5.00',  href:'gift-cards.html',    badge:''},
    {icon:'💿', name:'Software',      from:'From $4.99',  href:'software.html',      badge:'sale'},
    {icon:'💰', name:'Top Up',        from:'From $0.99',  href:'top-up.html',        badge:'hot'},
    {icon:'⚔️', name:'Game Items',    from:'From $1.99',  href:'game-items.html',    badge:''},
    {icon:'👤', name:'Accounts',      from:'From $6.99',  href:'accounts.html',      badge:'new'},
  ];
  const grid = document.getElementById('catGrid');
  if (grid) grid.innerHTML = cats.map(c => `
    <a href="${c.href}" class="cat-card" style="text-decoration:none">
      ${c.badge ? `<div class="cat-badge"><div class="badge-${c.badge}">${c.badge.toUpperCase()}</div></div>` : ''}
      <span class="cat-icon">${c.icon}</span>
      <div class="cat-name">${c.name}</div>
      <div class="cat-from">${c.from}</div>
    </a>`).join('');
});
</script>''')

# ── 2. GAMES ────────────────────────────────────────────────────
pages["games.html"] = page("Games", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Gaming Marketplace</div>
    <h1>🎮 Games</h1>
    <p>Premium titles, indie gems, and exclusive bundles for every platform.</p>
  </div>

  <div class="games-featured">
    <div class="game-featured-card gfc-1">
      <div class="gfc-icon">🏆</div>
      <div class="gfc-content">
        <div class="gfc-genre">Action RPG • PC / Console</div>
        <div class="gfc-title">The Blackened Realm — Ultimate Edition</div>
        <button class="btn-buy" style="margin-top:12px"
          onclick="openCheckout({name:'The Blackened Realm',cat:'Action RPG',price:'$59',icon:'🏆',badge:'hot'})">Buy $59.99</button>
      </div>
    </div>
    <div class="game-featured-card gfc-2">
      <div class="gfc-icon">🚀</div>
      <div class="gfc-content">
        <div class="gfc-genre">Space Strategy • PC</div>
        <div class="gfc-title">Stellar Command: Deep Space Expansion</div>
        <button class="btn-buy" style="margin-top:12px"
          onclick="openCheckout({name:'Stellar Command: Deep Space',cat:'Space Strategy',price:'$29',icon:'🚀',badge:''})">Buy $29.99</button>
      </div>
    </div>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterGames('all',this)">All Games</div>
    <div class="cat-pill" onclick="filterGames('Action',this)">Action</div>
    <div class="cat-pill" onclick="filterGames('RPG',this)">RPG</div>
    <div class="cat-pill" onclick="filterGames('Strategy',this)">Strategy</div>
    <div class="cat-pill" onclick="filterGames('Sports',this)">Sports</div>
    <div class="cat-pill" onclick="filterGames('Indie',this)">Indie</div>
    <div class="cat-pill" onclick="filterGames('Sandbox',this)">Sandbox</div>
    <div class="cat-pill" onclick="filterGames('Space',this)">Space</div>
  </div>
  <div class="product-grid" id="gamesGrid"></div>

  <div class="promo-banner" style="margin-top:48px">
    <div>
      <div class="promo-tag">Weekend Deal</div>
      <div class="promo-title">INDIE BUNDLE <span>— SAVE 35%</span></div>
      <div class="promo-sub">10 handpicked indie gems. Keys delivered instantly.</div>
    </div>
    <button class="btn-hero-primary"
      onclick="openCheckout({name:'Indie Bundle x10',cat:'Game Bundle',price:'$29',old:'$45',icon:'🎮',badge:'sale'})">Get Bundle →</button>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('gamesGrid', products.games));
function filterGames(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.games : products.games.filter(p => p.cat.toLowerCase().includes(cat.toLowerCase()));
  renderGrid('gamesGrid', filtered.length ? filtered : products.games);
}
</script>''')

# ── 3. GIFT CARDS ────────────────────────────────────────────────
pages["gift-cards.html"] = page("Gift Cards", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Digital Gift Cards</div>
    <h1>🎁 Gift Cards</h1>
    <p>The perfect gift for every gamer, creator &amp; digital enthusiast. Delivered in seconds.</p>
  </div>

  <div class="promo-banner" style="margin-bottom:40px">
    <div>
      <div class="promo-tag">New Stock</div>
      <div class="promo-title">GIFT CARDS <span>RESTOCKED</span></div>
      <div class="promo-sub">PlayStation, Xbox, Steam, Google Play, Apple — all in stock now</div>
    </div>
    <button class="btn-hero-primary" onclick="window.scrollTo({top:500,behavior:'smooth'})">Shop Now →</button>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterGifts('all',this)">All</div>
    <div class="cat-pill" onclick="filterGifts('PlayStation',this)">PlayStation</div>
    <div class="cat-pill" onclick="filterGifts('Xbox',this)">Xbox</div>
    <div class="cat-pill" onclick="filterGifts('Steam',this)">Steam</div>
    <div class="cat-pill" onclick="filterGifts('Google Play',this)">Google Play</div>
    <div class="cat-pill" onclick="filterGifts('Apple',this)">Apple</div>
    <div class="cat-pill" onclick="filterGifts('Amazon',this)">Amazon</div>
    <div class="cat-pill" onclick="filterGifts('Nintendo',this)">Nintendo</div>
    <div class="cat-pill" onclick="filterGifts('Roblox',this)">Roblox</div>
  </div>
  <div class="product-grid" id="giftGrid"></div>

  <div style="margin-top:64px;padding:40px;background:var(--card);border:1px solid var(--border);border-radius:8px;text-align:center">
    <div style="font-size:36px;margin-bottom:16px">💌</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:28px;letter-spacing:2px;color:var(--white);margin-bottom:8px">How It Works</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px;margin-top:32px;text-align:left">
      <div style="display:flex;gap:14px;align-items:flex-start">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:36px;color:var(--gold);flex-shrink:0">01</div>
        <div><div style="font-weight:700;color:var(--white);margin-bottom:4px">Choose a Card</div><div style="font-size:13px;color:#555">Pick your platform and desired value</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:36px;color:var(--gold);flex-shrink:0">02</div>
        <div><div style="font-weight:700;color:var(--white);margin-bottom:4px">Checkout Securely</div><div style="font-size:13px;color:#555">Pay with card, PayPal, or crypto</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:36px;color:var(--gold);flex-shrink:0">03</div>
        <div><div style="font-weight:700;color:var(--white);margin-bottom:4px">Instant Delivery</div><div style="font-size:13px;color:#555">Code sent to email in seconds</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:flex-start">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:36px;color:var(--gold);flex-shrink:0">04</div>
        <div><div style="font-weight:700;color:var(--white);margin-bottom:4px">Redeem &amp; Enjoy</div><div style="font-size:13px;color:#555">Apply code on your platform store</div></div>
      </div>
    </div>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('giftGrid', products.giftcards));
function filterGifts(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.giftcards : products.giftcards.filter(p => p.cat===cat);
  renderGrid('giftGrid', filtered.length ? filtered : products.giftcards);
}
</script>''')

# ── 4. SOFTWARE ──────────────────────────────────────────────────
pages["software.html"] = page("Software", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Digital Software</div>
    <h1>💿 Software</h1>
    <p>Licenses, activation keys, and subscriptions for top-tier software. Instant delivery.</p>
  </div>

  <div class="promo-banner" style="margin-bottom:40px">
    <div>
      <div class="promo-tag">Best Seller</div>
      <div class="promo-title">WINDOWS 11 PRO <span>— ONLY $19</span></div>
      <div class="promo-sub">Genuine license key, instant delivery. Retail value $199.</div>
    </div>
    <button class="btn-hero-primary"
      onclick="openCheckout({name:'Windows 11 Pro Key',cat:'OS License',price:'$19',old:'$199',icon:'💻',badge:'sale'})">Get It Now →</button>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterSoft('all',this)">All</div>
    <div class="cat-pill" onclick="filterSoft('OS',this)">OS / Windows</div>
    <div class="cat-pill" onclick="filterSoft('Design',this)">Design</div>
    <div class="cat-pill" onclick="filterSoft('Security',this)">Security</div>
    <div class="cat-pill" onclick="filterSoft('Productivity',this)">Productivity</div>
    <div class="cat-pill" onclick="filterSoft('VPN',this)">VPN</div>
    <div class="cat-pill" onclick="filterSoft('Utility',this)">Utility</div>
  </div>
  <div class="product-grid" id="softGrid"></div>

  <div style="margin-top:64px;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px">
    <div class="outsource-card">
      <div class="outsource-icon">🔑</div>
      <div class="outsource-title">Genuine Keys Only</div>
      <div class="outsource-desc">Every software key is sourced from official channels and tested before listing. No grey-market risk.</div>
    </div>
    <div class="outsource-card">
      <div class="outsource-icon">⚡</div>
      <div class="outsource-title">Instant Activation</div>
      <div class="outsource-desc">Keys delivered the moment payment clears. Activate your software in minutes, any time of day.</div>
    </div>
    <div class="outsource-card">
      <div class="outsource-icon">🔄</div>
      <div class="outsource-title">Replacement Guarantee</div>
      <div class="outsource-desc">If a key fails, contact us within 72 hours. We replace it immediately — no questions asked.</div>
    </div>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('softGrid', products.softwares));
function filterSoft(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.softwares : products.softwares.filter(p => p.cat.toLowerCase().includes(cat.toLowerCase()));
  renderGrid('softGrid', filtered.length ? filtered : products.softwares);
}
</script>''')

# ── 5. AI TOOLS ──────────────────────────────────────────────────
pages["ai-tools.html"] = page("AI Tools", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Artificial Intelligence</div>
    <h1>🤖 AI Tools</h1>
    <p>Cutting-edge AI subscriptions and tools for creators, developers, and professionals.</p>
  </div>

  <div class="promo-banner" style="margin-bottom:40px">
    <div>
      <div class="promo-tag">Limited Time</div>
      <div class="promo-title">AI TOOLS <span>BUNDLE</span></div>
      <div class="promo-sub">Get ChatGPT Plus + Midjourney + Claude Pro — save 40%</div>
    </div>
    <button class="btn-hero-primary"
      onclick="openCheckout({name:'AI Mega Bundle',cat:'Bundle',price:'$39',icon:'🤖',badge:'sale'})">Grab Bundle →</button>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterAI('all',this)">All AI</div>
    <div class="cat-pill" onclick="filterAI('AI Assistant',this)">Assistants</div>
    <div class="cat-pill" onclick="filterAI('AI Image',this)">Image Gen</div>
    <div class="cat-pill" onclick="filterAI('AI Video',this)">Video Gen</div>
    <div class="cat-pill" onclick="filterAI('AI Voice',this)">Voice AI</div>
    <div class="cat-pill" onclick="filterAI('AI Search',this)">AI Search</div>
  </div>
  <div class="product-grid" id="aiGrid"></div>

  <div style="margin-top:64px">
    <div class="section-title" style="font-size:32px;margin-bottom:24px">Why Buy <span>AI Subscriptions</span> Here?</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px">
      <div class="outsource-card">
        <div class="outsource-icon">⚡</div>
        <div class="outsource-title">Instant Activation</div>
        <div class="outsource-desc">Receive your login or key within seconds of payment. No waiting, no delays.</div>
      </div>
      <div class="outsource-card">
        <div class="outsource-icon">💰</div>
        <div class="outsource-title">Lower Prices</div>
        <div class="outsource-desc">Save up to 40% compared to buying directly from the provider through our bulk pricing model.</div>
      </div>
      <div class="outsource-card">
        <div class="outsource-icon">✅</div>
        <div class="outsource-title">Verified &amp; Authentic</div>
        <div class="outsource-desc">Every subscription is sourced directly from official channels and fully verified by our team.</div>
      </div>
    </div>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('aiGrid', products.aitools));
function filterAI(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.aitools : products.aitools.filter(p => p.cat.includes(cat));
  renderGrid('aiGrid', filtered.length ? filtered : products.aitools);
}
</script>''')

# ── 6. GAME ITEMS ────────────────────────────────────────────────
pages["game-items.html"] = page("Game Items", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">In-Game Marketplace</div>
    <h1>⚔️ Game Items</h1>
    <p>Skins, weapons, characters, currencies, and rare in-game assets. All verified.</p>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterItems('all',this)">All Items</div>
    <div class="cat-pill" onclick="filterItems('Skin',this)">Skins</div>
    <div class="cat-pill" onclick="filterItems('Weapon',this)">Weapons</div>
    <div class="cat-pill" onclick="filterItems('Character',this)">Characters</div>
    <div class="cat-pill" onclick="filterItems('Currency',this)">Currency</div>
    <div class="cat-pill" onclick="filterItems('Emote',this)">Emotes</div>
    <div class="cat-pill" onclick="filterItems('Bundle',this)">Bundles</div>
    <div class="cat-pill" onclick="filterItems('Melee',this)">Melee</div>
  </div>
  <div class="product-grid" id="itemsGrid"></div>

  <div class="promo-banner" style="margin-top:48px">
    <div>
      <div class="promo-tag">Rare Drop</div>
      <div class="promo-title">CS2 <span>DRAGON LORE AWP</span></div>
      <div class="promo-sub">Factory New — one of the rarest skins in Counter-Strike history</div>
    </div>
    <button class="btn-hero-primary"
      onclick="openCheckout({name:'CS2 Dragon Lore AWP',cat:'Weapon Skin',price:'$299',icon:'🐉',badge:'hot'})">Acquire Now →</button>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('itemsGrid', products.gameitems));
function filterItems(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.gameitems : products.gameitems.filter(p => p.cat.toLowerCase().includes(cat.toLowerCase()));
  renderGrid('itemsGrid', filtered.length ? filtered : products.gameitems);
}
</script>''')

# ── 7. ACCOUNTS ──────────────────────────────────────────────────
pages["accounts.html"] = page("Accounts", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Premium Accounts</div>
    <h1>👤 Accounts</h1>
    <p>Premium accounts for top streaming, gaming, and productivity platforms — verified and ready.</p>
  </div>

  <div style="background:linear-gradient(135deg,#0d1a10,#0a0a0a);border:1px solid rgba(0,230,118,0.2);border-radius:8px;padding:24px 32px;margin-bottom:32px;display:flex;align-items:center;gap:16px">
    <span style="font-size:32px">🛡️</span>
    <div>
      <div style="font-size:16px;font-weight:700;color:var(--white)">Account Guarantee</div>
      <div style="font-size:13px;color:#555;margin-top:4px">All accounts are manually tested before delivery. Full replacement guarantee within 24 hours if any issue occurs.</div>
    </div>
  </div>

  <div class="cat-strip">
    <div class="cat-pill active" onclick="filterAccts('all',this)">All</div>
    <div class="cat-pill" onclick="filterAccts('Streaming',this)">Streaming</div>
    <div class="cat-pill" onclick="filterAccts('Music',this)">Music</div>
    <div class="cat-pill" onclick="filterAccts('Design',this)">Design</div>
    <div class="cat-pill" onclick="filterAccts('Education',this)">Education</div>
    <div class="cat-pill" onclick="filterAccts('Writing',this)">Writing</div>
  </div>
  <div class="product-grid" id="acctGrid"></div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('acctGrid', products.accounts));
function filterAccts(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.accounts : products.accounts.filter(p => p.cat===cat || p.cat.toLowerCase().includes(cat.toLowerCase()));
  renderGrid('acctGrid', filtered.length ? filtered : products.accounts);
}
</script>''')

# ── 8. SUBSCRIPTIONS ─────────────────────────────────────────────
pages["subscriptions.html"] = page("Subscriptions", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Digital Subscriptions</div>
    <h1>📋 Subscriptions</h1>
    <p>Gaming passes, creative suites, streaming bundles — subscribe at the best price.</p>
  </div>

  <div class="section-title" style="font-size:28px;margin-bottom:8px">Choose Your <span>PlayBeat Plan</span></div>
  <div style="font-family:'Share Tech Mono',monospace;font-size:11px;color:#444;letter-spacing:2px;margin-bottom:32px">UNLOCK EXCLUSIVE DEALS AND PRIORITY ACCESS</div>

  <div class="sub-grid">
    <div class="sub-card">
      <div class="plan-name">Starter</div>
      <div class="plan-price">$9<span style="font-size:20px">.99</span></div>
      <div class="plan-per">/ month</div>
      <ul class="plan-features">
        <li class="included">Access to 500+ products</li>
        <li class="included">Standard delivery</li>
        <li class="included">Email support</li>
        <li>Prime badge</li>
        <li>Exclusive deals</li>
        <li>Priority queue</li>
      </ul>
      <button class="btn-plan" onclick="openModal('signupModal')">Get Started</button>
    </div>
    <div class="sub-card featured-plan">
      <div class="plan-badge">Most Popular</div>
      <div class="plan-name">Prime</div>
      <div class="plan-price">$24<span style="font-size:20px">.99</span></div>
      <div class="plan-per">/ month</div>
      <ul class="plan-features">
        <li class="included">Access to ALL products</li>
        <li class="included">Instant delivery</li>
        <li class="included">24/7 priority support</li>
        <li class="included">Prime badge + exclusive deals</li>
        <li class="included">Early access to releases</li>
        <li>Team management (5 seats)</li>
      </ul>
      <button class="btn-plan" onclick="openModal('signupModal')">Upgrade to Prime</button>
    </div>
    <div class="sub-card">
      <div class="plan-name">Enterprise</div>
      <div class="plan-price">$99<span style="font-size:20px">.99</span></div>
      <div class="plan-per">/ month</div>
      <ul class="plan-features">
        <li class="included">Everything in Prime</li>
        <li class="included">Unlimited seats</li>
        <li class="included">Dedicated account manager</li>
        <li class="included">Custom integrations</li>
        <li class="included">Bulk purchasing</li>
        <li class="included">White-label options</li>
      </ul>
      <button class="btn-plan" onclick="window.location.href='contact.html'">Contact Sales</button>
    </div>
  </div>

  <div style="margin-top:64px">
    <div class="section-title" style="font-size:28px;margin-bottom:24px">Available <span>Subscriptions</span></div>
    <div class="cat-strip">
      <div class="cat-pill active" onclick="filterSubs('all',this)">All</div>
      <div class="cat-pill" onclick="filterSubs('Gaming',this)">Gaming</div>
      <div class="cat-pill" onclick="filterSubs('Creative',this)">Creative</div>
      <div class="cat-pill" onclick="filterSubs('Streaming',this)">Streaming</div>
      <div class="cat-pill" onclick="filterSubs('Security',this)">Security</div>
      <div class="cat-pill" onclick="filterSubs('Productivity',this)">Productivity</div>
    </div>
    <div class="product-grid" id="subProductGrid"></div>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('subProductGrid', products.subs));
function filterSubs(cat, el) {
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const filtered = cat==='all' ? products.subs : products.subs.filter(p => p.cat===cat);
  renderGrid('subProductGrid', filtered.length ? filtered : products.subs);
}
</script>''')

# ── 9. TOP UP ────────────────────────────────────────────────────
pages["top-up.html"] = page("Top Up", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Instant Recharge</div>
    <h1>💰 Top Up</h1>
    <p>Recharge your gaming wallets, mobile credits, and platform balances instantly.</p>
  </div>

  <div style="margin-bottom:32px;font-family:'Share Tech Mono',monospace;font-size:11px;color:#444;letter-spacing:2px">SELECT PLATFORM</div>
  <div class="topup-platforms" id="topupGrid"></div>

  <div class="section-title" style="font-size:28px;margin-bottom:24px">Select <span>Amount</span></div>
  <div class="cat-strip" id="amountStrip">
    <div class="cat-pill" onclick="setAmount(5,this)">$5</div>
    <div class="cat-pill" onclick="setAmount(10,this)">$10</div>
    <div class="cat-pill active" onclick="setAmount(25,this)">$25</div>
    <div class="cat-pill" onclick="setAmount(50,this)">$50</div>
    <div class="cat-pill" onclick="setAmount(100,this)">$100</div>
    <div class="cat-pill" onclick="setAmount(0,this)">Custom</div>
  </div>

  <div style="max-width:480px;margin-top:32px">
    <div class="form-group">
      <label class="form-label">Game / Platform ID</label>
      <input class="form-input" type="text" id="topupId" placeholder="Enter your ID or username">
    </div>
    <div class="form-group">
      <label class="form-label">Server (if applicable)</label>
      <input class="form-input" type="text" id="topupServer" placeholder="e.g. NA, EU, ASIA">
    </div>
    <div class="form-group" id="customAmtGroup" style="display:none">
      <label class="form-label">Custom Amount ($)</label>
      <input class="form-input" type="number" id="customAmt" placeholder="Enter amount" min="1">
    </div>
    <button class="btn-hero-primary" style="width:100%;padding:14px" id="topupBtn" onclick="doTopUp()">⚡ Top Up Now — $25.00</button>
  </div>
</div>
''', extra_js='''<script>
let selectedAmt = 25;
let selectedPlatform = null;
document.addEventListener('DOMContentLoaded', () => {
  const grid = document.getElementById('topupGrid');
  if (grid) grid.innerHTML = products.topupPlatforms.map(p => `
    <div class="topup-card" onclick="selectPlatform('${p.name}','${p.icon}',this)">
      <div class="icon">${p.icon}</div>
      <div class="name">${p.name}</div>
      <div class="hint">${p.hint}</div>
    </div>`).join('');
});
function selectPlatform(name, icon, el) {
  document.querySelectorAll('.topup-card').forEach(c => c.style.borderColor='');
  el.style.borderColor = 'var(--gold)';
  selectedPlatform = {name, icon};
}
function setAmount(amt, el) {
  document.querySelectorAll('#amountStrip .cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  const cg = document.getElementById('customAmtGroup');
  if (amt === 0) { selectedAmt = null; cg.style.display='block'; }
  else { selectedAmt = amt; cg.style.display='none'; document.getElementById('topupBtn').textContent = `⚡ Top Up Now — $${amt}.00`; }
}
function doTopUp() {
  const id = document.getElementById('topupId').value.trim();
  if (!selectedPlatform) { alert('Please select a platform first.'); return; }
  if (!id) { alert('Please enter your game/platform ID.'); return; }
  const amt = selectedAmt || parseInt(document.getElementById('customAmt').value) || 0;
  if (!amt) { alert('Please select or enter an amount.'); return; }
  openCheckout({name: `${selectedPlatform.name} Top Up $${amt}`, cat: 'Top Up', price: `$${amt}`, icon: selectedPlatform.icon, badge: ''});
}
</script>''')

# ── 10. TRENDING ─────────────────────────────────────────────────
pages["trending.html"] = page("Trending", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">What\'s Hot Right Now</div>
    <h1>🔥 Trending</h1>
    <p>The most-purchased digital products this week across all categories.</p>
  </div>

  <div class="stats-row">
    <div class="stat-card"><div class="num">12K+</div><div class="lbl">Orders This Week</div></div>
    <div class="stat-card"><div class="num">4.9★</div><div class="lbl">Average Rating</div></div>
    <div class="stat-card"><div class="num">98%</div><div class="lbl">Satisfied Buyers</div></div>
    <div class="stat-card"><div class="num">&lt;2s</div><div class="lbl">Avg Delivery Time</div></div>
  </div>

  <div class="tab-bar">
    <button class="tab-btn active" onclick="switchTab(this,'tab-all')">All</button>
    <button class="tab-btn" onclick="switchTab(this,'tab-games')">Games</button>
    <button class="tab-btn" onclick="switchTab(this,'tab-ai')">AI Tools</button>
    <button class="tab-btn" onclick="switchTab(this,'tab-subs')">Subscriptions</button>
    <button class="tab-btn" onclick="switchTab(this,'tab-items')">Game Items</button>
  </div>
  <div id="tab-all" class="tab-content active">
    <div class="product-grid" id="trendAllGrid"></div>
  </div>
  <div id="tab-games" class="tab-content">
    <div class="product-grid" id="trendGamesGrid"></div>
  </div>
  <div id="tab-ai" class="tab-content">
    <div class="product-grid" id="trendAIGrid"></div>
  </div>
  <div id="tab-subs" class="tab-content">
    <div class="product-grid" id="trendSubsGrid"></div>
  </div>
  <div id="tab-items" class="tab-content">
    <div class="product-grid" id="trendItemsGrid"></div>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => {
  renderGrid('trendAllGrid', products.trending);
  renderGrid('trendGamesGrid', products.games);
  renderGrid('trendAIGrid', products.aitools);
  renderGrid('trendSubsGrid', products.subs);
  renderGrid('trendItemsGrid', products.gameitems);
});
</script>''')

# ── 11. BEST VALUE ────────────────────────────────────────────────
pages["best-value.html"] = page("Best Value", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Maximum Value</div>
    <h1>💎 Best Value</h1>
    <p>Highest-rated products at the lowest price-to-quality ratio. Curated by our team weekly.</p>
  </div>

  <div style="background:linear-gradient(135deg,#0a100a,#0a0a0a);border:1px solid rgba(0,230,118,0.15);border-radius:8px;padding:24px 32px;margin-bottom:40px;display:flex;align-items:center;gap:16px">
    <span style="font-size:32px">🏷️</span>
    <div>
      <div style="font-size:15px;font-weight:700;color:var(--white)">Why These Products?</div>
      <div style="font-size:13px;color:#555;margin-top:4px">Our team scores every product on quality, customer satisfaction, and savings vs. retail — these are the top performers.</div>
    </div>
  </div>

  <div class="product-grid" id="bestGrid"></div>

  <div style="margin-top:64px;text-align:center;padding:48px;background:var(--card);border:1px solid var(--border);border-radius:8px">
    <div style="font-family:'Bebas Neue',sans-serif;font-size:32px;letter-spacing:3px;color:var(--white);margin-bottom:8px">Want <span style="color:var(--gold)">Even More</span> Value?</div>
    <p style="font-size:14px;color:#555;margin-bottom:24px">Prime members get early access to flash sales and exclusive bundle deals not available to the public.</p>
    <button class="btn-hero-primary" onclick="openModal('signupModal')">Join Prime Free →</button>
  </div>
</div>
''', extra_js='''<script>
document.addEventListener('DOMContentLoaded', () => renderGrid('bestGrid', products.bestvalue));
</script>''')

# ── 12. OUTSOURCE ─────────────────────────────────────────────────
pages["outsource.html"] = page("Outsource", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Digital Services</div>
    <h1>🛠️ Outsource</h1>
    <p>Hire vetted experts for game boosts, digital design, account setup, and more.</p>
  </div>

  <div class="outsource-hero">
    <div style="position:relative;z-index:2">
      <div style="font-family:'Share Tech Mono',monospace;font-size:11px;letter-spacing:3px;color:var(--gold);margin-bottom:16px">POWERED BY PRIME MEMBERS</div>
      <div style="font-family:'Bebas Neue',sans-serif;font-size:52px;letter-spacing:3px;color:var(--white);line-height:1;margin-bottom:16px">
        EXPERT SERVICES<br><span style="color:var(--gold)">ON DEMAND</span>
      </div>
      <p style="font-size:16px;color:#666;max-width:560px;margin:0 auto">Connect with vetted PlayBeat professionals for game boosting, account setup, digital design, and strategic services.</p>
      <div style="display:flex;gap:16px;justify-content:center;margin-top:32px">
        <button class="btn-hero-primary" onclick="openModal('signupModal')">Browse Services →</button>
        <button class="btn-hero-secondary" onclick="openModal('signupModal')">Become a Seller</button>
      </div>
    </div>
  </div>

  <div class="outsource-grid">
    <div class="outsource-card" onclick="openCheckout({name:'Valorant Rank Boost to Diamond',cat:'Game Boost',price:'$49',icon:'🎯',badge:''})">
      <div class="outsource-icon">🎯</div>
      <div class="outsource-title">Game Rank Boosting</div>
      <div class="outsource-desc">Climb the ranked ladder in Valorant, CS2, League of Legends, and more. Fast, discreet, guaranteed.</div>
      <div class="outsource-price">FROM $19 · EST. 24–72 HOURS</div>
    </div>
    <div class="outsource-card" onclick="openCheckout({name:'Professional Logo Design',cat:'Design',price:'$39',icon:'🎨',badge:''})">
      <div class="outsource-icon">🎨</div>
      <div class="outsource-title">Digital Design</div>
      <div class="outsource-desc">Logos, thumbnails, social media kits, and stream overlays by professional designers.</div>
      <div class="outsource-price">FROM $29 · EST. 48 HOURS</div>
    </div>
    <div class="outsource-card" onclick="openCheckout({name:'Account Setup & Configuration',cat:'Setup',price:'$15',icon:'⚙️',badge:''})">
      <div class="outsource-icon">⚙️</div>
      <div class="outsource-title">Account Setup</div>
      <div class="outsource-desc">Full configuration of your new platform accounts — security, preferences, linked services.</div>
      <div class="outsource-price">FROM $9 · EST. 1–3 HOURS</div>
    </div>
    <div class="outsource-card" onclick="openCheckout({name:'Gaming Strategy Coaching 1hr',cat:'Coaching',price:'$25',icon:'📈',badge:''})">
      <div class="outsource-icon">📈</div>
      <div class="outsource-title">Gaming Coaching</div>
      <div class="outsource-desc">1-on-1 coaching sessions with ranked pro players. Improve mechanics, game sense, and strategy.</div>
      <div class="outsource-price">FROM $25/HR · FLEXIBLE SCHEDULE</div>
    </div>
    <div class="outsource-card" onclick="openCheckout({name:'Content Creation Package',cat:'Content',price:'$59',icon:'📹',badge:''})">
      <div class="outsource-icon">📹</div>
      <div class="outsource-title">Content Creation</div>
      <div class="outsource-desc">Highlight reels, stream clips, YouTube thumbnails, and social media content by creators.</div>
      <div class="outsource-price">FROM $39 · EST. 2–5 DAYS</div>
    </div>
    <div class="outsource-card" onclick="openCheckout({name:'VPN Setup & Privacy Config',cat:'IT Service',price:'$19',icon:'🔒',badge:''})">
      <div class="outsource-icon">🔒</div>
      <div class="outsource-title">IT &amp; Security Setup</div>
      <div class="outsource-desc">VPN configuration, two-factor authentication setup, and digital privacy audits.</div>
      <div class="outsource-price">FROM $12 · EST. 30–60 MIN</div>
    </div>
  </div>
</div>
''')

# ── 13. OUR TEAM ──────────────────────────────────────────────────
pages["our-team.html"] = page("Our Team", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">The People Behind PlayBeat</div>
    <h1>👥 Our Team</h1>
    <p>World-class experts in digital commerce, gaming, and technology.</p>
  </div>

  <div class="stats-row" style="margin-bottom:64px">
    <div class="stat-card"><div class="num">42</div><div class="lbl">Team Members</div></div>
    <div class="stat-card"><div class="num">18</div><div class="lbl">Countries</div></div>
    <div class="stat-card"><div class="num">7yrs</div><div class="lbl">In Business</div></div>
    <div class="stat-card"><div class="num">500K+</div><div class="lbl">Happy Customers</div></div>
  </div>

  <div class="team-grid">
    <div class="team-card">
      <div class="team-avatar">👨‍💼</div>
      <div class="team-name">Alex Carter</div>
      <div class="team-role">CEO &amp; Founder</div>
      <div class="team-bio">15 years in digital marketplace innovation. Built PlayBeat from the ground up with a vision for frictionless digital commerce.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">👩‍💻</div>
      <div class="team-name">Zara Patel</div>
      <div class="team-role">CTO</div>
      <div class="team-bio">Former Lead Engineer at major tech firms. Architects our platform\'s security and instant-delivery infrastructure.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">🧑‍🎨</div>
      <div class="team-name">Marcus Lee</div>
      <div class="team-role">Head of Design</div>
      <div class="team-bio">Creates the visual language of PlayBeat. Passionate about dark UI, futurism, and immersive digital experiences.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">👩‍🔬</div>
      <div class="team-name">Sofia Reyes</div>
      <div class="team-role">Head of AI Products</div>
      <div class="team-bio">PhD in Machine Learning. Curates and validates every AI tool on our platform for quality and authenticity.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">🧑‍💼</div>
      <div class="team-name">James Wright</div>
      <div class="team-role">VP of Partnerships</div>
      <div class="team-bio">Manages relationships with over 200 game publishers, software vendors, and AI companies worldwide.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">👨‍🎮</div>
      <div class="team-name">Kai Tanaka</div>
      <div class="team-role">Gaming Director</div>
      <div class="team-bio">Competitive gaming veteran. Ensures our gaming catalog stays ahead of the market with exclusive deals.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">👩‍⚖️</div>
      <div class="team-name">Amina Hassan</div>
      <div class="team-role">Head of Compliance</div>
      <div class="team-bio">Legal expert ensuring all products meet international compliance and consumer protection standards.</div>
    </div>
    <div class="team-card">
      <div class="team-avatar">👨‍🛠️</div>
      <div class="team-name">Luca Moretti</div>
      <div class="team-role">Head of Support</div>
      <div class="team-bio">Built our 24/7 support infrastructure from scratch. Average response time: under 5 minutes for Prime members.</div>
    </div>
  </div>

  <div style="margin-top:64px;text-align:center;padding:48px;background:var(--card);border:1px solid var(--border);border-radius:8px">
    <div style="font-size:36px;margin-bottom:16px">🚀</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:28px;letter-spacing:2px;color:var(--white);margin-bottom:8px">We\'re <span style="color:var(--gold)">Hiring</span></div>
    <p style="font-size:14px;color:#555;margin-bottom:24px">Join our global team of digital commerce pioneers. Remote-friendly, competitive compensation.</p>
    <a href="contact.html" class="btn-hero-primary">View Open Roles →</a>
  </div>
</div>
''')

# ── 14. FAQ ───────────────────────────────────────────────────────
pages["faq.html"] = page("FAQ", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">Help Center</div>
    <h1>❓ Frequently Asked Questions</h1>
    <p>Find answers to the most common questions about PlayBeat Digital.</p>
  </div>

  <div class="faq-grid">
    <div>
      <div style="font-family:'Share Tech Mono',monospace;font-size:10px;letter-spacing:2px;color:var(--gold);text-transform:uppercase;margin-bottom:20px">Ordering &amp; Delivery</div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">How do I receive my product after purchase? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">After checkout, your product key or account credentials are delivered instantly to your PlayBeat account (under My Orders) and to your registered email address. No waiting required.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">How long does delivery take? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Delivery is truly instant — your key appears the moment payment is confirmed. Our average delivery time is under 2 seconds. If there\'s any delay, contact our support team immediately.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">What payment methods do you accept? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">We accept all major credit/debit cards (Visa, Mastercard, Amex), PayPal, Apple Pay, Google Pay, and several cryptocurrencies including Bitcoin, Ethereum, and USDT.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">Can I buy for someone else as a gift? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Yes! Simply forward the key or credentials to the recipient after purchase. For gift cards, they\'re universally redeemable and make perfect digital gifts.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">What regions are supported? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">PlayBeat supports 100+ countries. Product listings clearly indicate if there are regional restrictions. We stock region-specific and global variants for most popular products.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">Do I need an account to purchase? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">You need a free PlayBeat account to complete a purchase. This ensures your order history is safely stored and you can access your keys at any time from My Account.</div>
      </div>
    </div>

    <div>
      <div style="font-family:'Share Tech Mono',monospace;font-size:10px;letter-spacing:2px;color:var(--gold);text-transform:uppercase;margin-bottom:20px">Products &amp; Refunds</div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">Are all products genuine and authentic? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Absolutely. Every product on PlayBeat is sourced through official channels and manually verified by our quality assurance team before being listed. We maintain a strict zero-tolerance policy for invalid keys.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">What if my key doesn\'t work? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">We offer a full replacement guarantee. If your key is invalid or already used, contact support within 72 hours with your order ID and we\'ll resolve it immediately — no questions asked.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">Can I get a refund? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Digital products are non-refundable once delivered. However, if a product is defective or invalid, we provide a free replacement. See our <a href="refund.html" style="color:var(--gold)">Refund Policy</a> for details.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">How does PlayBeat Prime membership work? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Prime membership gives you access to exclusive deals, early product access, priority customer support, and a Prime badge on your profile. Plans start at $9.99/month — see <a href="subscriptions.html" style="color:var(--gold)">Subscriptions</a>.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">Is my payment information secure? <span class="faq-arrow">▼</span></div>
        <div class="faq-a">Yes. We use 256-bit SSL encryption on all transactions. PlayBeat never stores your full card details — payments are processed through PCI-DSS compliant payment processors.</div>
      </div>
    </div>
  </div>

  <div style="text-align:center;margin-top:64px;padding:48px;background:var(--card);border:1px solid var(--border);border-radius:8px">
    <div style="font-size:32px;margin-bottom:16px">💬</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:28px;letter-spacing:2px;color:var(--white);margin-bottom:8px">Still Have Questions?</div>
    <p style="font-size:14px;color:#555;margin-bottom:24px">Our support team is online 24/7 — average response time under 5 minutes.</p>
    <a href="contact.html" class="btn-hero-primary">Contact Support →</a>
  </div>
</div>
''', extra_js='''<script>
function toggleFaq(el) {
  const item = el.parentElement;
  const answer = item.querySelector('.faq-a');
  const arrow = el.querySelector('.faq-arrow');
  const isOpen = item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i => {
    i.classList.remove('open');
    i.querySelector('.faq-a').style.display = 'none';
    const a = i.querySelector('.faq-arrow');
    if (a) a.textContent = '▼';
  });
  if (!isOpen) {
    item.classList.add('open');
    answer.style.display = 'block';
    if (arrow) arrow.textContent = '▲';
  }
}
</script>''')

# ── 15. CONTACT ───────────────────────────────────────────────────
pages["contact.html"] = page("Contact", '''
<div class="main">
  <div class="page-header">
    <div class="eyebrow">We\'re Here For You</div>
    <h1>📞 Contact Us</h1>
    <p>Support available 24/7. Average response time: under 5 minutes for Prime members.</p>
  </div>

  <div class="contact-grid">
    <div>
      <div class="contact-info-item">
        <div class="contact-info-icon">💬</div>
        <div>
          <div class="contact-info-label">Live Chat</div>
          <div class="contact-info-val">Available Now</div>
          <div class="contact-info-sub">Fastest option — respond in &lt;5 min</div>
          <button class="btn-hero-primary" style="margin-top:12px;padding:10px 24px">Start Chat →</button>
        </div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-icon">📧</div>
        <div>
          <div class="contact-info-label">Email Support</div>
          <div class="contact-info-val">support@playbeat.digital</div>
          <div class="contact-info-sub">Response within 1 hour</div>
        </div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-icon">🐦</div>
        <div>
          <div class="contact-info-label">Twitter / X</div>
          <div class="contact-info-val">@PlayBeatDigital</div>
          <div class="contact-info-sub">DMs open for support</div>
        </div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-icon">💬</div>
        <div>
          <div class="contact-info-label">Discord</div>
          <div class="contact-info-val">discord.gg/playbeat</div>
          <div class="contact-info-sub">Community + dedicated support channel</div>
        </div>
      </div>
    </div>

    <div>
      <div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;letter-spacing:2px;color:var(--gold);text-transform:uppercase;margin-bottom:20px">Send a Message</div>
      <div class="form-group"><label class="form-label">Your Name</label><input class="form-input" type="text" id="ctName" placeholder="Alex Carter"></div>
      <div class="form-group"><label class="form-label">Email Address</label><input class="form-input" type="email" id="ctEmail" placeholder="you@email.com"></div>
      <div class="form-group">
        <label class="form-label">Subject</label>
        <select class="form-input" id="ctSubject" style="cursor:pointer">
          <option>Order Issue</option>
          <option>Invalid Key</option>
          <option>Billing Question</option>
          <option>Partnership Enquiry</option>
          <option>General Question</option>
          <option>Other</option>
        </select>
      </div>
      <div class="form-group"><label class="form-label">Order ID (if applicable)</label><input class="form-input" type="text" id="ctOrder" placeholder="PB-XXXXXXXX"></div>
      <div class="form-group"><label class="form-label">Message</label><textarea class="form-textarea" id="ctMsg" placeholder="Describe your issue or question in detail…"></textarea></div>
      <div id="ctSuccess" style="color:var(--green);font-family:\'Share Tech Mono\',monospace;font-size:12px;margin-bottom:12px;display:none">✓ Message sent! We\'ll reply within 1 hour.</div>
      <button class="btn-hero-primary" style="width:100%;padding:14px" onclick="sendContact()">Send Message →</button>
    </div>
  </div>
</div>
''', extra_js='''<script>
function sendContact() {
  const name  = document.getElementById('ctName').value.trim();
  const email = document.getElementById('ctEmail').value.trim();
  const msg   = document.getElementById('ctMsg').value.trim();
  if (!name || !email || !msg) { alert('Please fill in all required fields.'); return; }
  const btn = document.querySelector('.contact-grid button.btn-hero-primary');
  if (btn) { btn.textContent = '⏳ Sending…'; btn.disabled = true; }
  setTimeout(() => {
    if (btn) { btn.textContent = 'Send Message →'; btn.disabled = false; }
    document.getElementById('ctSuccess').style.display = 'block';
    ['ctName','ctEmail','ctMsg','ctOrder'].forEach(id => { const el=document.getElementById(id); if(el) el.value=''; });
  }, 1200);
}
</script>''')

# ── 16. MY ACCOUNT ────────────────────────────────────────────────
pages["my-account.html"] = page("My Account", '''
<div class="main" style="padding-top:40px;padding-bottom:80px">
  <div id="acctGate" style="text-align:center;padding:80px 0;display:none">
    <div style="font-size:64px;margin-bottom:24px">🔒</div>
    <div style="font-family:\'Bebas Neue\',sans-serif;font-size:36px;letter-spacing:3px;color:var(--white);margin-bottom:12px">Sign In Required</div>
    <p style="font-size:15px;color:#555;margin-bottom:32px">Create a free account or sign in to manage your orders, wishlist, and profile.</p>
    <div style="display:flex;gap:16px;justify-content:center">
      <button class="btn-hero-primary" onclick="openModal(\'signinModal\')">Sign In →</button>
      <button class="btn-hero-secondary" onclick="openModal(\'signupModal\')">Create Account</button>
    </div>
  </div>

  <div id="acctContent">
    <div class="myacct-header">
      <div class="myacct-avatar-big" id="acctAvatarBig">👤</div>
      <div class="myacct-info">
        <h2 id="acctFullName">User Name</h2>
        <div class="email" id="acctEmail">user@email.com</div>
        <div class="tier">⭐ Prime Member</div>
      </div>
    </div>

    <div class="acct-tabs">
      <button class="acct-tab active" onclick="switchAcctTab(this,\'tab-orders\')">📦 Orders</button>
      <button class="acct-tab" onclick="switchAcctTab(this,\'tab-wishlist\')">♡ Wishlist</button>
      <button class="acct-tab" onclick="switchAcctTab(this,\'tab-profile\')">⚙️ Profile</button>
    </div>

    <div class="acct-panel active" id="tab-orders">
      <div id="ordersEmpty" style="text-align:center;padding:60px;color:#444">
        <div style="font-size:48px;margin-bottom:16px">📦</div>
        <div style="font-family:\'Bebas Neue\',sans-serif;font-size:24px;letter-spacing:2px">No orders yet</div>
        <div style="font-size:14px;margin-top:8px">Start shopping to see your orders here</div>
        <a href="index.html" class="btn-hero-primary" style="display:inline-block;margin-top:20px;padding:12px 28px;border-radius:4px">Browse Products</a>
      </div>
      <div id="ordersList"></div>
    </div>

    <div class="acct-panel" id="tab-wishlist">
      <div id="wishlistEmpty" style="text-align:center;padding:60px;color:#444">
        <div style="font-size:48px;margin-bottom:16px">♡</div>
        <div style="font-family:\'Bebas Neue\',sans-serif;font-size:24px;letter-spacing:2px">Wishlist is empty</div>
        <div style="font-size:14px;margin-top:8px">Tap the ♡ on any product to save it</div>
      </div>
      <div class="wishlist-grid" id="wishlistItems"></div>
    </div>

    <div class="acct-panel" id="tab-profile">
      <div style="max-width:480px">
        <div class="form-group"><label class="form-label">First Name</label><input class="form-input" id="profileFirst" type="text"></div>
        <div class="form-group"><label class="form-label">Last Name</label><input class="form-input" id="profileLast"  type="text"></div>
        <div class="form-group"><label class="form-label">Email</label><input class="form-input" id="profileEmail" type="email"></div>
        <div class="form-group">
          <label class="form-label">New Password <span style="color:#444;font-size:11px">(leave blank to keep current)</span></label>
          <input class="form-input" type="password" placeholder="••••••••">
        </div>
        <button class="btn-hero-primary" style="padding:12px 32px;border-radius:4px" onclick="saveProfile()">Save Changes</button>
        <button class="btn-login" style="margin-left:12px;padding:12px 24px;border-radius:4px" onclick="doLogout()">🚪 Logout</button>
      </div>
    </div>
  </div>
</div>
''', extra_js='''<script>
function updateAccountPage() {
  if (!currentUser) {
    document.getElementById('acctContent').style.display = 'none';
    document.getElementById('acctGate').style.display = 'block';
    return;
  }
  document.getElementById('acctGate').style.display = 'none';
  document.getElementById('acctContent').style.display = 'block';
  document.getElementById('acctFullName').textContent = currentUser.first + ' ' + currentUser.last;
  document.getElementById('acctEmail').textContent = currentUser.email;
  document.getElementById('profileFirst').value = currentUser.first;
  document.getElementById('profileLast').value = currentUser.last;
  document.getElementById('profileEmail').value = currentUser.email;
  renderOrders();
  renderWishlistItems();
}

function renderOrders() {
  const list = document.getElementById('ordersList');
  const empty = document.getElementById('ordersEmpty');
  if (!list) return;
  if (orders.length === 0) {
    empty && (empty.style.display = 'block');
    list.innerHTML = '';
  } else {
    empty && (empty.style.display = 'none');
    list.innerHTML = orders.map(o => `
      <div class="order-row">
        <div style="display:flex;align-items:center">
          <div class="order-icon">${o.icon}</div>
          <div><div class="order-name">${o.name}</div><div class="order-date">${o.status} · ${o.date}</div></div>
        </div>
        <div style="display:flex;align-items:center;gap:16px">
          <div style="font-family:'Bebas Neue',sans-serif;font-size:20px;color:var(--gold)">${o.price}</div>
          <div class="order-status status-active">Active</div>
        </div>
      </div>`).join('');
  }
}

function renderWishlistItems() {
  const grid = document.getElementById('wishlistItems');
  const empty = document.getElementById('wishlistEmpty');
  if (!grid) return;
  if (wishlist.length === 0) {
    empty && (empty.style.display = 'block');
    grid.innerHTML = '';
  } else {
    empty && (empty.style.display = 'none');
    grid.innerHTML = wishlist.map(p => `
      <div class="product-card">
        <div class="product-card-img">${p.icon}</div>
        <div class="product-card-body">
          <div class="product-name">${p.name}</div>
          <div class="product-cat">${p.cat}</div>
          <div class="product-price-row">
            <div class="product-price">${p.price}</div>
            <div style="display:flex;gap:6px">
              <button class="btn-buy" onclick='openCheckout(${JSON.stringify(p)})'>Buy</button>
              <button onclick='toggleWishlist(${JSON.stringify(p)})' style="background:none;border:1px solid #333;border-radius:2px;color:#c33;cursor:pointer;padding:6px 8px;font-size:12px" title="Remove">✕</button>
            </div>
          </div>
        </div>
      </div>`).join('');
  }
}

document.addEventListener('DOMContentLoaded', updateAccountPage);
</script>''')

# ── 17. PRIVACY ───────────────────────────────────────────────────
pages["privacy.html"] = page("Privacy Policy", '''
<div class="main" style="padding-top:40px;padding-bottom:80px">
  <div class="page-header">
    <div class="eyebrow">Legal</div>
    <h1>🔒 Privacy Policy</h1>
    <p>Last updated: January 1, 2026</p>
  </div>
  <div class="privacy-content">
    <h3>1. Information We Collect</h3>
    <p>We collect information you provide directly to us, such as your name, email address, and payment details when you create an account or make a purchase. We also automatically collect certain information when you use our services, including IP addresses, browser type, pages visited, and transaction data.</p>
    <h3>2. How We Use Your Information</h3>
    <p>We use the information we collect to process transactions, send order confirmations, provide customer support, improve our services, and comply with legal obligations. We do not sell your personal data to third parties.</p>
    <h3>3. Data Storage &amp; Security</h3>
    <p>Your data is stored on secure servers with 256-bit SSL encryption. Payment card details are never stored on our servers — all transactions are processed through PCI-DSS compliant payment processors. We retain your data only as long as necessary to provide our services.</p>
    <h3>4. Cookies</h3>
    <p>We use cookies to keep you signed in, remember your preferences, and analyze site traffic. You can disable cookies in your browser settings, though some features may not function properly.</p>
    <h3>5. Your Rights</h3>
    <p>You have the right to access, correct, or delete your personal data at any time. To exercise these rights, contact us at privacy@playbeat.digital. We will respond within 30 days.</p>
    <h3>6. Third-Party Services</h3>
    <p>Our platform integrates with third-party services including payment processors and analytics providers. These services have their own privacy policies, which we encourage you to review.</p>
    <h3>7. Contact Us</h3>
    <p>If you have questions about this Privacy Policy, contact us at privacy@playbeat.digital or through our <a href="contact.html" style="color:var(--gold)">Contact page</a>.</p>
  </div>
</div>
''')

# ── 18. TERMS ─────────────────────────────────────────────────────
pages["terms.html"] = page("Terms of Service", '''
<div class="main" style="padding-top:40px;padding-bottom:80px">
  <div class="page-header">
    <div class="eyebrow">Legal</div>
    <h1>📄 Terms of Service</h1>
    <p>Last updated: January 1, 2026. Please read these terms carefully.</p>
  </div>
  <div class="privacy-content">
    <h3>1. Acceptance of Terms</h3>
    <p>By accessing or using PlayBeat Digital ("the Service"), you agree to be bound by these Terms of Service and all applicable laws and regulations. If you do not agree, you may not use the Service.</p>
    <h3>2. Digital Products</h3>
    <p>All products sold on PlayBeat are digital goods delivered electronically. Upon successful payment, your key or credentials are delivered instantly. You are responsible for redeeming the product within any stated validity period.</p>
    <h3>3. Account Responsibility</h3>
    <p>You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. Notify us immediately of any unauthorized use.</p>
    <h3>4. Prohibited Uses</h3>
    <p>You may not use the Service for any unlawful purpose, to resell digital products without authorization, to attempt to circumvent security measures, or to engage in fraudulent transactions.</p>
    <h3>5. Limitation of Liability</h3>
    <p>PlayBeat Digital is not liable for any indirect, incidental, or consequential damages arising from your use of the Service. Our total liability is limited to the amount you paid for the specific product in question.</p>
    <h3>6. Governing Law</h3>
    <p>These terms are governed by the laws of the jurisdiction in which PlayBeat Digital operates. Any disputes will be resolved through binding arbitration.</p>
    <h3>7. Changes to Terms</h3>
    <p>We reserve the right to update these terms at any time. Continued use of the Service after changes constitutes acceptance of the new terms.</p>
  </div>
</div>
''')

# ── 19. REFUND ────────────────────────────────────────────────────
pages["refund.html"] = page("Refund Policy", '''
<div class="main" style="padding-top:40px;padding-bottom:80px">
  <div class="page-header">
    <div class="eyebrow">Legal</div>
    <h1>💳 Refund Policy</h1>
    <p>Last updated: January 1, 2026</p>
  </div>
  <div class="privacy-content">
    <h3>Digital Products — General Policy</h3>
    <p>Due to the nature of digital goods, all sales are final once the product has been delivered. However, we offer a full replacement guarantee for any product that is defective, invalid, or already used at the time of delivery.</p>
    <h3>Replacement Guarantee</h3>
    <p>If your product key is invalid, already redeemed, or does not work as described, contact our support team within 72 hours of purchase with your order ID. We will verify and replace the product at no additional cost — no questions asked.</p>
    <h3>Exceptions</h3>
    <p>Replacements are not provided if: the key has been successfully redeemed and then you change your mind; the product was used by you and later banned due to a violation of the game\'s/platform\'s terms of service; or the order is older than 72 hours without prior contact.</p>
    <h3>Account &amp; Subscription Products</h3>
    <p>For account products, the replacement window is 24 hours from delivery. If an account stops working due to actions taken by you (password changes, security violations), no replacement is provided.</p>
    <h3>How to Request a Replacement</h3>
    <p>Contact us via our <a href="contact.html" style="color:var(--gold)">Contact page</a>, provide your Order ID, and describe the issue. Our team aims to resolve all replacement requests within 1 hour.</p>
    <h3>Payment Disputes</h3>
    <p>Initiating a chargeback without first contacting our support team will result in account suspension. We strongly encourage contacting us first as we resolve virtually all issues within hours.</p>
  </div>
</div>
''')

# ─── WRITE ALL FILES ─────────────────────────────────────────────

for filename, content in pages.items():
    path = OUT / filename
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ {filename}")

print(f"\n✅ Generated {len(pages)} HTML files in ./{OUT}/")
print(f"   + shared.css and shared.js copied")
print(f"\n   Open dist/index.html in your browser to preview.")
print(f"\n   Pages generated:")
for f in sorted(pages.keys()):
    print(f"     • {f}")
