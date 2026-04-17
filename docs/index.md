<style>
  /* --- STRICT PREMIUM BRAND SYSTEM --- */
  .portfolio-container {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: #1E293B; /* Primary text */
    background-color: #FAF9F6; /* Soft ivory bg */
    line-height: 1.6;
    padding: 1rem;
  }

  /* Hero Section */
  .hero-section {
    background-color: #0B132B; /* Midnight navy */
    color: #F8FAFC; /* Light text on dark */
    padding: 3.5rem 2rem;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 30px rgba(11, 19, 43, 0.15); /* Shadow using Navy */
    border-bottom: 4px solid #D4AF37; /* Luxury gold accent */
  }

  .hero-section h1 {
    color: #F8FAFC !important;
    font-size: 2.8rem;
    margin-bottom: 0.5rem;
    font-weight: 800;
    letter-spacing: -0.5px;
  }

  .hero-section h2 {
    color: #00E5FF !important; /* Electric cyan highlight */
    font-size: 1.4rem;
    font-weight: 500;
    margin-top: 0;
  }

  /* Contact Chips */
  .contact-chips {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.5rem;
  }

  .chip {
    background-color: rgba(248, 250, 252, 0.05); /* Transparent light text color */
    border: 1px solid #00E5FF; /* Cyan border */
    color: #F8FAFC;
    padding: 0.5rem 1.2rem;
    border-radius: 50px;
    font-size: 0.9rem;
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .chip:hover {
    background-color: #00E5FF;
    color: #0B132B; /* Navy text on cyan hover */
    transform: translateY(-2px);
  }

  /* Quote Box */
  .premium-quote {
    background-color: #F1F5F9; /* Card background */
    border-left: 5px solid #D4AF37; /* Gold accent */
    padding: 1.5rem 2rem;
    font-style: italic;
    font-size: 1.1rem;
    color: #1E293B;
    margin: 2rem 0;
    border-radius: 0 8px 8px 0;
  }

  /* Section Headings */
  .section-title {
    color: #0B132B; /* Navy Headings */
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  /* Cards Grid */
  .cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .premium-card {
    background-color: #F1F5F9; /* Card background (No pure white) */
    border: 1px solid rgba(11, 19, 43, 0.1); /* Navy transparent border */
    border-top: 4px solid #0B132B; /* Navy top border */
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(11, 19, 43, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .premium-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(11, 19, 43, 0.1);
    border-top-color: #D4AF37; /* Hover changes to Gold */
  }

  .premium-card h4 {
    color: #0B132B;
    margin-top: 0;
    font-size: 1.2rem;
    border-bottom: 1px solid rgba(11, 19, 43, 0.1);
    padding-bottom: 0.5rem;
  }

  /* Table Styling */
  .premium-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    background-color: #F1F5F9; /* Card background */
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(11, 19, 43, 0.05);
  }

  .premium-table th {
    background-color: #0B132B; /* Navy */
    color: #F8FAFC; /* Light text */
    padding: 1rem;
    text-align: left;
  }

  .premium-table td {
    padding: 1rem;
    border-bottom: 1px solid rgba(11, 19, 43, 0.1);
    color: #1E293B;
  }

  .premium-table tr:hover {
    background-color: #FAF9F6; /* Ivory hover */
  }

  /* Bullet Lists */
  .custom-list {
    list-style: none;
    padding-left: 0;
  }

  .custom-list li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 0.8rem;
    color: #1E293B;
  }

  .custom-list li::before {
    content: '■';
    color: #D4AF37; /* Gold bullets */
    position: absolute;
    left: 0;
    top: 2px;
    font-size: 0.8rem;
  }

  /* CTA Box */
  .cta-box {
    background-color: #0B132B; /* Navy background */
    color: #F8FAFC;
    text-align: center;
    padding: 3rem 2rem;
    border-radius: 12px;
    margin-top: 4rem;
    border: 1px solid rgba(212, 175, 55, 0.3); /* Subtle Gold border */
  }

  .cta-button {
    display: inline-block;
    background-color: #00E5FF; /* High Visibility CTA */
    color: #0B132B; /* Navy text for contrast */
    font-weight: 700;
    padding: 1rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    margin-top: 1.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
  }

  .cta-button:hover {
    background-color: #D4AF37; /* Cyan shifts to Gold on hover */
    color: #0B132B;
    transform: scale(1.05);
  }
</style>

<div class="portfolio-container">

  <div class="hero-section">
    <h1>Dr. Sandeep Shrivastava</h1>
    <h2>The Healthcare-AI Visionary & Automation Architect</h2>
    <p style="margin-top: 1rem; font-size: 1.1rem; opacity: 0.9;">
      Ayurvedic Doctor | Dietitian | Child Care & Education Specialist <br> Healthcare Business Coach | AI Automation Expert
    </p>
    
    <div class="contact-chips">
      <a href="mailto:ask@allhelp.in" class="chip">📧 ask@allhelp.in</a>
      <a href="tel:9140415046" class="chip">📞 9140415046</a>
      <a href="https://www.linkedin.com/in/dr-sandeep-shrivastva-6a206429b" target="_blank" class="chip">🔗 LinkedIn</a>
      <a href="https://whatsapp.com/channel/0029Va5tFCoGZNClobRrOQ15" target="_blank" class="chip">📱 WhatsApp Channel</a>
      <a href="https://t.me/medpreneur" target="_blank" class="chip">📱 Telegram</a>
    </div>
  </div>

  <div class="section-title">🚀 The Complete AI Automation Ecosystem Builder</div>
  <p>Dr. Sandeep Shrivastava is a <strong>revolutionary force</strong> at the intersection of <strong>traditional Ayurvedic wisdom</strong> and <strong>cutting-edge artificial intelligence</strong>. He hasn't just learned technology—he has <strong>mastered the art of execution</strong>, building a self-sustaining automation empire that bridges ancient healthcare with futuristic innovation.</p>
  
  <div class="premium-quote">
    "Not just coding. Not just tools. A complete system. The focus is never just basic Q&A; it is about building robust <strong>Automation Pipelines</strong> that execute real work."
  </div>

  <div class="section-title">⚡ Technical & Clinical Mastery</div>
  <div class="cards-grid">
    <div class="premium-card">
      <h4>🤖 AI & Tech Arsenal</h4>
      <ul style="padding-left: 1rem;">
        <li><strong>Local AI:</strong> OpenClaw & Ollama (Zero Dependency)</li>
        <li><strong>RAG Systems:</strong> Advanced Vector DB Implementation</li>
        <li><strong>AI Agents:</strong> LangChain & CrewAI Specialist</li>
        <li><strong>Automation:</strong> n8n Expert & Telegram Bots</li>
        <li><strong>Web Tech:</strong> HTML, CSS, Python, Java</li>
      </ul>
    </div>
    
    <div class="premium-card">
      <h4>🏥 Traditional Medicine Authority</h4>
      <ul style="padding-left: 1rem;">
        <li><strong>BAMS Graduate:</strong> Govt. Ayurveda Medical College</li>
        <li><strong>Certified:</strong> Nutrition & Health Education</li>
        <li><strong>Published Author:</strong> 300+ Ebooks & 5+ Physical Books</li>
        <li><strong>Educator:</strong> Created 50+ Professional Courses</li>
      </ul>
    </div>
  </div>

  <div class="section-title">💡 Ventures & Professional Services</div>
  <div class="cards-grid">
    <div class="premium-card">
      <h4>Healthcare Ventures</h4>
      <p>Founder & Owner of:</p>
      <ul style="padding-left: 1rem;">
        <li><strong>MedPreneurs</strong> (Startup Ecosystem)</li>
        <li><strong>DeepLifeCourse</strong> (Deep Learning)</li>
        <li><strong>Bhojdeep</strong> (Nutritional Wisdom)</li>
        <li><strong>GrowDeep & HealthDeep</strong></li>
      </ul>
    </div>

    <div class="premium-card">
      <h4>Consultancy Offered</h4>
      <ul style="padding-left: 1rem;">
        <li><strong>Business Coaching:</strong> Incubation & Strategy</li>
        <li><strong>AI Implementation:</strong> Automation Pipelines</li>
        <li><strong>Training:</strong> Ayurveda & Digital Transformation</li>
      </ul>
    </div>
  </div>

  <div class="section-title">🛠️ Diverse Skill Portfolio</div>
  <table class="premium-table">
    <thead>
      <tr>
        <th style="width: 25%;">Category</th>
        <th>Core Skills</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Technical</strong></td>
        <td>Data Analysis, Python, Java, HTML, CSS, API Integration</td>
      </tr>
      <tr>
        <td><strong>AI/ML</strong></td>
        <td>LangChain, CrewAI, RAG Systems, Vector DB, Ollama, OpenClaw</td>
      </tr>
      <tr>
        <td><strong>Automation</strong></td>
        <td>n8n, Workflow Automation, Telegram Bots, Content Engine</td>
      </tr>
      <tr>
        <td><strong>Business</strong></td>
        <td>Project/HR Management, Digital Marketing, Productivity</td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">🌟 Why Collaborate with Dr. Sandeep?</div>
  <ul class="custom-list">
    <li><strong>Unique Value Proposition:</strong> The only professional combining <em>Deep Ayurvedic Knowledge + Modern Medical Education + Advanced AI Technical Skills + Proven Business Acumen</em>.</li>
    <li><strong>Execution-Focused:</strong> Not just theory—built 300+ books, 50+ courses, multiple platforms, and complete automation systems.</li>
    <li><strong>Self-Sufficient Ecosystem:</strong> Runs local AI environments, creates content automatically, manages multiple ventures—true independence.</li>
    <li><strong>Innovation Leader:</strong> From traditional manuscripts to AI agents—spanning the complete spectrum of healthcare evolution.</li>
  </ul>

  <div class="cta-box">
    <h2 style="margin: 0; color: #F8FAFC; font-size: 2rem;">Ready to build real AI systems?</h2>
    <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem;">Transforming healthcare through technology. Building real systems, not just wrappers.</p>
    <a href="mailto:ask@allhelp.in" class="cta-button">📩 Contact ask@allhelp.in</a>
    <p style="margin-top: 1.5rem; font-style: italic; opacity: 0.7;">"This is not learning. This is execution." 🚀</p>
  </div>

</div>