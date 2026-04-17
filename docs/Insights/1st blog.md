<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PureMDX | Pioneering Prevention Intelligence - Dr. Sandeep Shrivastava</title>
    <link href="https://fonts.googleapis.com/css2?family=Cambria&family=Georgia&display=swap" rel="stylesheet">
    <style>
        :root {
            --royal-blue: rgb(0, 112, 192);
            --deep-navy: rgb(0, 32, 96);
            --vibrant-orange: rgb(255, 153, 0);
            --gold: rgb(218, 165, 32);
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-card: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --border-color: #e2e8f0;
            --shadow-color: rgba(0, 0, 0, 0.1);
            --shadow-deep: rgba(0, 0, 0, 0.15);
        }

        [data-theme="dark"] {
            --bg-primary: rgb(0, 32, 96);
            --bg-secondary: rgb(0, 50, 120);
            --bg-card: rgb(0, 60, 140);
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --border-color: rgba(255, 255, 255, 0.2);
            --shadow-color: rgba(0, 0, 0, 0.4);
            --shadow-deep: rgba(0, 0, 0, 0.5);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Georgia, 'Times New Roman', serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.7;
            transition: background-color 0.3s ease, color 0.3s ease;
            max-width: 600px;
            margin: 0 auto;
            padding: 0 16px 120px;
        }

        /* Sticky Header with PureMDX Branding */
        .brand-header {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: linear-gradient(135deg, var(--royal-blue), var(--deep-navy));
            border-radius: 0 0 20px 20px;
            padding: 20px;
            margin: 0 -16px 30px;
            box-shadow: 0 4px 20px var(--shadow-deep);
        }

        .brand-header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .puremdx-logo {
            font-family: Cambria, Georgia, serif;
            font-size: 1.8rem;
            font-weight: 800;
            color: white;
            letter-spacing: 1px;
        }

        .puremdx-tagline {
            font-family: Arial, sans-serif;
            font-size: 0.75rem;
            color: var(--vibrant-orange);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 600;
        }

        .author-credentials {
            background: rgba(255, 255, 255, 0.1);
            border-left: 3px solid var(--vibrant-orange);
            border-radius: 8px;
            padding: 12px;
            margin-top: 12px;
        }

        .author-name {
            font-family: Cambria, Georgia, serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: white;
            margin-bottom: 4px;
        }

        .author-title {
            font-family: Arial, sans-serif;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.4;
        }

        .author-title span {
            display: block;
            margin-top: 2px;
            font-size: 0.75rem;
            color: var(--vibrant-orange);
            font-weight: 600;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 30px 0;
            border-bottom: 3px solid var(--gold);
            margin-bottom: 30px;
        }

        .hero h1 {
            font-family: Cambria, Georgia, serif;
            font-size: 1.9rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 16px;
            color: var(--royal-blue);
        }

        .hero p {
            color: var(--text-secondary);
            font-size: 1.05rem;
            max-width: 95%;
            margin: 0 auto;
            font-style: italic;
        }

        /* Table of Contents - Gold Accent */
        .toc {
            background: var(--bg-card);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 32px;
            box-shadow: 0 4px 20px var(--shadow-color);
            border: 2px solid var(--gold);
            position: relative;
        }

        .toc::before {
            content: '📚';
            position: absolute;
            top: -15px;
            left: 20px;
            background: var(--bg-card);
            padding: 0 10px;
            font-size: 1.2rem;
        }

        .toc h2 {
            font-family: Cambria, Georgia, serif;
            font-size: 1.3rem;
            font-weight: 800;
            margin-bottom: 20px;
            color: var(--gold);
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .toc-list {
            list-style: none;
        }

        .toc-list li {
            margin-bottom: 10px;
        }

        .toc-list a {
            display: block;
            padding: 14px 16px;
            background: var(--bg-primary);
            border-radius: 12px;
            text-decoration: none;
            color: var(--text-primary);
            font-family: Arial, sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            border: 1px solid var(--border-color);
            min-height: 48px;
            display: flex;
            align-items: center;
            border-left: 4px solid var(--vibrant-orange);
        }

        .toc-list a:hover, .toc-list a:active {
            background: var(--royal-blue);
            color: white;
            transform: translateX(6px);
            border-left-color: var(--gold);
        }

        /* Cards */
        .card {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 28px;
            margin-bottom: 24px;
            box-shadow: 0 8px 32px var(--shadow-color);
            border: 1px solid var(--border-color);
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.4s ease;
            position: relative;
        }

        .card.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--royal-blue), var(--vibrant-orange));
            border-radius: 20px 20px 0 0;
        }

        .card h2 {
            font-family: Cambria, Georgia, serif;
            font-size: 1.5rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.3;
            color: var(--royal-blue);
        }

        .card h3 {
            font-family: Cambria, Georgia, serif;
            font-size: 1.15rem;
            font-weight: 700;
            margin: 24px 0 12px;
            color: var(--deep-navy);
            border-bottom: 2px solid var(--vibrant-orange);
            padding-bottom: 8px;
            display: inline-block;
        }

        .card p {
            color: var(--text-secondary);
            margin-bottom: 16px;
            font-size: 0.98rem;
            text-align: justify;
        }

        /* Bullet Points */
        .bullet-list {
            list-style: none;
            margin: 16px 0;
        }

        .bullet-list li {
            padding: 14px 0;
            padding-left: 40px;
            position: relative;
            color: var(--text-secondary);
            font-size: 0.95rem;
            border-bottom: 1px solid var(--border-color);
            line-height: 1.6;
        }

        .bullet-list li:last-child {
            border-bottom: none;
        }

        .bullet-list li::before {
            position: absolute;
            left: 0;
            font-size: 1.3rem;
            top: 50%;
            transform: translateY(-50%);
        }

        .bullet-list li[data-icon="rocket"]::before { content: "🚀"; }
        .bullet-list li[data-icon="check"]::before { content: "✅"; }
        .bullet-list li[data-icon="lightbulb"]::before { content: "💡"; }
        .bullet-list li[data-icon="warning"]::before { content: "⚠️"; }
        .bullet-list li[data-icon="target"]::before { content: "🎯"; }

        /* Key Takeaway Box */
        .takeaway {
            background: linear-gradient(135deg, rgba(0, 112, 192, 0.1), rgba(255, 153, 0, 0.1));
            border: 2px dashed var(--vibrant-orange);
            border-radius: 16px;
            padding: 20px;
            margin: 24px 0;
            position: relative;
        }

        .takeaway::before {
            content: '★';
            position: absolute;
            top: -12px;
            right: 20px;
            background: var(--bg-card);
            color: var(--gold);
            font-size: 1.2rem;
            padding: 0 8px;
        }

        .takeaway h4 {
            font-family: Arial, sans-serif;
            font-size: 0.85rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--royal-blue);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .takeaway p {
            margin: 0;
            font-weight: 600;
            color: var(--text-primary);
            font-family: Georgia, serif;
        }

        /* PureMDX Footer Branding */
        .puremdx-footer {
            background: linear-gradient(135deg, var(--deep-navy), var(--royal-blue));
            border-radius: 20px 20px 0 0;
            padding: 30px 20px;
            margin: 40px -16px 0;
            text-align: center;
            color: white;
            position: relative;
        }

        .puremdx-footer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: var(--vibrant-orange);
            border-radius: 0 0 4px 4px;
        }

        .footer-logo {
            font-family: Cambria, Georgia, serif;
            font-size: 1.6rem;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
            letter-spacing: 2px;
        }

        .footer-mission {
            font-family: Arial, sans-serif;
            font-size: 0.85rem;
            color: var(--vibrant-orange);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 700;
            margin-bottom: 16px;
        }

        .footer-author {
            font-family: Georgia, serif;
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 4px;
        }

        .footer-creds {
            font-family: Arial, sans-serif;
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.5;
        }

        /* Floating Action Buttons */
        .fab-container {
            position: fixed;
            bottom: 24px;
            right: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            z-index: 1000;
        }

        .fab {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            box-shadow: 0 4px 20px var(--shadow-deep);
            transition: all 0.3s ease;
            background: var(--vibrant-orange);
            color: white;
        }

        .fab:hover, .fab:active {
            transform: scale(1.1);
            box-shadow: 0 6px 30px var(--shadow-deep);
        }

        .fab-back-to-top {
            opacity: 0;
            visibility: hidden;
            transform: translateY(20px);
            background: var(--royal-blue);
        }

        .fab-back-to-top.visible {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }

        .fab-theme {
            background: var(--deep-navy);
        }

        /* Preface Special Styling */
        .preface {
            border-left: 4px solid var(--royal-blue);
            background: linear-gradient(135deg, var(--bg-card), var(--bg-primary));
        }

        /* Conclusion */
        .conclusion {
            background: linear-gradient(135deg, rgba(0, 112, 192, 0.05), rgba(255, 153, 0, 0.05));
            border: 2px solid var(--royal-blue);
        }

        /* Acknowledgement */
        .acknowledgement {
            text-align: center;
            padding: 20px;
            font-style: italic;
            color: var(--text-secondary);
            font-size: 0.9rem;
            border-top: 1px solid var(--border-color);
            margin-top: 20px;
        }

        /* Responsive adjustments */
        @media (max-width: 480px) {
            .puremdx-logo {
                font-size: 1.5rem;
            }
            
            .hero h1 {
                font-size: 1.6rem;
            }
            
            .card {
                padding: 20px;
            }
            
            .card h2 {
                font-size: 1.3rem;
            }
            
            .author-name {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <!-- Sticky Brand Header -->
    <header class="brand-header">
        <div class="brand-header-top">
            <div>
                <div class="puremdx-logo">PureMDX</div>
                <div class="puremdx-tagline">Pioneering Prevention Intelligence</div>
            </div>
        </div>
        <div class="author-credentials">
            <div class="author-name">Dr. Sandeep Shrivastava</div>
            <div class="author-title">
                BAMS (Govt. Ayurveda Medical College & Hospital Tvm Kerala)<br>
                DNHE (Diploma in Nutrition and Health Education)<br>
                <span>Founder: Medpreneurs</span>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>The Clinical Reality</h1>
        <p>A comprehensive analysis of the academic and practical struggles facing BAMS students in modern Ayurvedic education</p>
    </section>

    <!-- Table of Contents -->
    <nav class="toc">
        <h2>Table of Contents</h2>
        <ul class="toc-list">
            <li><a href="#chapter1">🏛️ Why Traditional Learning Models Are Failing</a></li>
            <li><a href="#chapter2">🏗️ Infrastructure Gaps Blocking Student Success</a></li>
            <li><a href="#chapter3">👥 The Patient Connection Crisis</a></li>
            <li><a href="#chapter4">🧠 Breaking the Confidence Barrier</a></li>
            <li><a href="#chapter5">📚 Fixing Broken Teaching Methods</a></li>
            <li><a href="#chapter6">🚧 Systemic Roadmaps to Clinical Access</a></li>
            <li><a href="#chapter7">✨ Blueprint for Educational Transformation</a></li>
            <li><a href="#chapter8">🎯 The Path Forward</a></li>
        </ul>
    </nav>

    <!-- Preface -->
    <section class="card preface" id="preface">
        <h2>💡 Why This Analysis Matters</h2>
        <p>The BAMS program represents a critical pipeline for healthcare professionals in India's traditional medicine sector. Yet a widening gap exists between theoretical knowledge and practical competency.</p>
        <p>This document examines systemic challenges including inadequate infrastructure, insufficient patient interaction opportunities, and the erosion of professional confidence.</p>
        <div class="takeaway">
            <h4>🎯 Core Mission</h4>
            <p>To inform stakeholders—university administrators, regulatory bodies, and students—about multidimensional challenges requiring urgent intervention.</p>
        </div>
    </section>

    <!-- Chapter 1 -->
    <section class="card" id="chapter1">
        <h2>🏛️ Why Traditional Learning Models Are Failing</h2>
        
        <h3>The Pedagogy Evolution Trap</h3>
        <p>Ayurvedic education has shifted from apprenticeship-based learning to standardized institutional models. This transition, while aiming for international standards, has reduced direct patient observation time.</p>
        <p>The pressure to complete rigorous academic schedules leaves little room for the slower, observational process essential to Ayurvedic diagnostics.</p>

        <h3>From Holistic Practice to Exam Anxiety</h3>
        <p>Students now prioritize memorization over intuitive diagnostic skills. The competitive environment fosters stress that detracts from well-being and learning.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Clinical practice is viewed as a hurdle rather than a learning opportunity</li>
            <li data-icon="lightbulb">The therapeutic relationship takes a backseat to academic grades</li>
            <li data-icon="rocket">Trust-building skills essential for patient management are neglected</li>
        </ul>

        <h3>The Promise vs. Reality Divide</h3>
        <p>Institutions claim high-quality clinical training but fail to provide necessary resources. The ratio of supervisors to students often exceeds safe educational limits.</p>
        
        <div class="takeaway">
            <h4>⚠️ Critical Gap</h4>
            <p>Students learn from observation but are denied practice due to liability concerns—producing graduates who can describe treatments but lack execution confidence.</p>
        </div>
    </section>

    <!-- Chapter 2 -->
    <section class="card" id="chapter2">
        <h2>🏗️ Infrastructure Gaps Blocking Student Success</h2>
        
        <h3>Facilities That Fail Future Healers</h3>
        <p>Many BAMS colleges operate in repurposed facilities lacking essential Ayurvedic training features. Proper herb storage requires specific humidity and temperature controls that are often unavailable.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Students learn pharmacology without smelling or handling raw materials</li>
            <li data-icon="lightbulb">Examination rooms lack privacy for pulse and tongue diagnosis</li>
            <li data-icon="rocket">Poor ventilation and lighting reduce capacity to observe subtle disease signs</li>
        </ul>

        <h3>The Bed Availability Crisis</h3>
        <p>Clinical bed ratios are critically high in private and semi-government colleges. Students rotate through departments but rarely manage a patient from admission to discharge.</p>
        
        <h3>Resource Scarcity Impact</h3>
        <p>Outdated equipment prevents accurate learning of diagnostic procedures. Students enter the workforce relying on intuition rather than trained muscle memory.</p>
        
        <div class="takeaway">
            <h4>🎯 The Bottom Line</h4>
            <p>Infrastructure deficits create hesitation when handling instruments and contribute to the low confidence observed among graduates entering practice.</p>
        </div>
    </section>

    <!-- Chapter 3 -->
    <section class="card" id="chapter3">
        <h2>👥 The Patient Connection Crisis</h2>
        
        <h3>Locked Out of Clinical Engagement</h3>
        <p>Ayurveda emphasizes the physician-patient relationship as the foundation of healing. Yet institutional structures prioritize lectures over clinical immersion.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Students are relegated to administrative tasks instead of patient interviews</li>
            <li data-icon="lightbulb">Exclusion from decision-making prevents development of chronic disease management skills</li>
            <li data-icon="rocket">The passive observer role erodes the desire to become a physician</li>
        </ul>

        <h3>Communication Barriers</h3>
        <p>Students lack training in managing patient anxiety or delivering difficult news within the Ayurvedic context. This hesitation strains the therapeutic alliance.</p>
        
        <h3>The Missing Mentorship</h3>
        <p>Overburdened attending physicians lack time to demonstrate communication skills. Students are expected to know outcomes without learning the diagnostic process.</p>
        
        <div class="takeaway">
            <h4>💡 Critical Insight</h4>
            <p>When supervisors interrupt without guidance, students develop cynicism and view patients as test cases rather than partners in care.</p>
        </div>
    </section>

    <!-- Chapter 4 -->
    <section class="card" id="chapter4">
        <h2>🧠 Breaking the Confidence Barrier</h2>
        
        <h3>The Imposter Syndrome Epidemic</h3>
        <p>The combination of academic rigor and practical deficits creates widespread imposter syndrome. Students internalize failures as personal incompetence rather than resource scarcity.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Clinical rounds become anxiety sources rather than learning opportunities</li>
            <li data-icon="lightbulb">Fear of errors leads to paralysis in decision-making</li>
            <li data-icon="rocket">Hesitation to suggest interventions delays treatment initiation</li>
        </ul>

        <h3>Diagnostic Fear Factor</h3>
        <p>Ayurveda's subjective diagnostic tools require repeated practice and immediate feedback. Without structured supervision, error rates remain high and confidence plummets.</p>
        
        <h3>The Mental Health Toll</h3>
        <p>Students witness suffering without emotional preparation tools. The lack of mental health support, combined with sleep deprivation and academic stress, leads to burnout.</p>
        
        <div class="takeaway">
            <h4>⚠️ Urgent Priority</h4>
            <p>The mental health crisis among medical students is an overlooked issue causing early dropout rates and attrition in the healthcare system.</p>
        </div>
    </section>

    <!-- Chapter 5 -->
    <section class="card" id="chapter5">
        <h2>📚 Fixing Broken Teaching Methods</h2>
        
        <h3>Textbook vs. Reality</h3>
        <p>Ayurveda requires touch, smell, taste, and observation. Yet the curriculum remains heavily text-based, preventing integration of knowledge with practice.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Students cannot map textbook descriptions to complex clinical realities</li>
            <li data-icon="lightbulb">Experiential learning is treated as elective rather than mandatory</li>
            <li data-icon="rocket">Months of memorization without immediate dispensary application</li>
        </ul>

        <h3>Fragmented Holistic Education</h3>
        <p>Diet, lifestyle, and environment are taught as separate modules rather than integrated components. Students know what the liver needs but not the patient's daily life.</p>
        
        <h3>Punitive Assessment Culture</h3>
        <p>Evaluation methods penalize risk-taking and discourage innovation. Students prefer rote memorization to avoid clinical failure in exams.</p>
        
        <div class="takeaway">
            <h4>🎯 Assessment Misalignment</h4>
            <p>Current evaluations test theoretical recall rather than clinical reasoning—producing academic achievers who are not competent practitioners.</p>
        </div>
    </section>

    <!-- Chapter 6 -->
    <section class="card" id="chapter6">
        <h2>🚧 Systemic Roadmaps to Clinical Access</h2>
        
        <h3>Regulatory Overreach</h3>
        <p>Patient safety guidelines, while well-intentioned, create overly cautious approaches that limit student exposure. Fear of litigation leads institutions to restrict hands-on components.</p>
        
        <ul class="bullet-list">
            <li data-icon="warning">Students learn procedures from diagrams rather than by doing</li>
            <li data-icon="lightbulb">Regulatory culture promotes fear rather than learning from safe errors</li>
            <li data-icon="rocket">Lack of confidence in handling emergencies results</li>
        </ul>

        <h3>Misplaced Institutional Priorities</h3>
        <p>Public funds for Ayurvedic colleges remain inadequate. Administration prioritizes enrollment expansion over clinical facility maintenance.</p>
        
        <h3>The Public Health Disconnect</h3>
        <p>A gap exists between government curriculum claims and actual student resources. Graduates cannot effectively contribute to the Ayurvedic healthcare system.</p>
        
        <div class="takeaway">
            <h4>⚠️ Systemic Failure</h4>
            <p>The government expects a competent workforce, but the educational system fails to produce one—creating a public health service gap.</p>
        </div>
    </section>

    <!-- Chapter 7 -->
    <section class="card" id="chapter7">
        <h2>✨ Blueprint for Educational Transformation</h2>
        
        <h3>Curriculum Reform Strategy</h3>
        <p>Restructure programs to prioritize practical integration. Theory courses should be delivered in modular formats allowing immediate clinical application.</p>
        
        <ul class="bullet-list">
            <li data-icon="rocket">Pulse reading lessons should immediately transition to dispensary practice</li>
            <li data-icon="check">Significantly increase time allocation for clinical rotations</li>
            <li data-icon="lightbulb">Establish dedicated teaching beds monitored specifically for education</li>
        </ul>

        <h3>Mentorship Programs</h3>
        <p>Senior practitioners should be paired with students for sustained guidance throughout clinical years. Supervisors must model professional behavior and provide constructive feedback.</p>
        
        <h3>Technology Integration</h3>
        <p>Virtual reality simulations can teach diagnostic procedures difficult to practice in hospitals. Digital tools can provide feedback on pulse and tongue reading accuracy.</p>
        
        <div class="takeaway">
            <h4>💡 Innovation Focus</h4>
            <p>Telemedicine platforms allow students to observe complex cases remotely when physical beds are unavailable—building resilient learning systems.</p>
        </div>
    </section>

    <!-- Chapter 8 -->
    <section class="card conclusion" id="chapter8">
        <h2>🎯 The Path Forward</h2>
        
        <p>The BAMS program aims to produce holistic healthcare professionals. Yet current challenges undermine graduate competency and threaten the profession's viability.</p>
        
        <p>The gap between academic requirements and clinical realities is too wide to ignore. Infrastructure deficits, limited clinical exposure, and insufficient mentorship create a workforce ill-equipped for modern healthcare complexities.</p>
        
        <ul class="bullet-list">
            <li data-icon="target">Educational systems must prioritize practical skills and student well-being</li>
            <li data-icon="check">Government and regulatory bodies must allocate resources for infrastructure</li>
            <li data-icon="rocket">Ayurveda must reclaim its roots in practice to remain relevant</li>
        </ul>
        
        <div class="takeaway">
            <h4>🚀 Call to Action</h4>
            <p>Without urgent intervention, the BAMS profession risks becoming an academic exercise rather than a viable healthcare option. The future of Ayurveda depends on these critical changes.</p>
        </div>
    </section>

    <!-- Acknowledgement -->
    <section class="acknowledgement">
        <p>With gratitude to the universities, institutions, and students who contributed to this analysis.</p>
    </section>

    <!-- PureMDX Footer Branding -->
    <footer class="puremdx-footer">
        <div class="footer-logo">PureMDX</div>
        <div class="footer-mission">The Future of Holistic Healing</div>
        <div class="footer-author">Dr. Sandeep Shrivastava</div>
        <div class="footer-creds">
            BAMS (Govt. Ayurveda Medical College & Hospital Tvm Kerala)<br>
            DNHE | Founder: Medpreneurs
        </div>
    </footer>

    <!-- Floating Action Buttons -->
    <div class="fab-container">
        <button class="fab fab-back-to-top" id="backToTop" title="Back to Top">↑</button>
        <button class="fab fab-theme" id="themeToggle" title="Toggle Theme">🌙</button>
    </div>

    <script>
        // Theme Toggle with localStorage
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        
        const savedTheme = localStorage.getItem('puremdx-theme');
        if (savedTheme) {
            html.setAttribute('data-theme', savedTheme);
            themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
        }
        
        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('puremdx-theme', newTheme);
            themeToggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
        });

        // Back to Top Button
        const backToTop = document.getElementById('backToTop');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });
        
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        // Intersection Observer for Fade-in Animations
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('.card').forEach(card => {
            observer.observe(card);
        });

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>