---
title: System Diagnostic Report
---


<style>

  .ai-canvas {
    background-color: #0f172a;
    color: #e2e8f0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 2rem;
    border-radius: 12px;
  }
  h1 {
    color: #38bdf8;
    border-bottom: 2px solid #334155;
    padding-bottom: 10px;
    font-size: 2.5rem;
  }
  .dashboard-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 25px;
  }
  .card {
    background: #1e293b;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.5);
    border-left: 5px solid #10b981;
    transition: transform 0.3s ease;
  }
  .card:hover {
    transform: translateY(-5px);
  }
  .card h3 { 
    color: #10b981; 
    margin-top: 0; 
    font-size: 1.5rem;
  }
  .status-badge {
    display: inline-block;
    padding: 4px 10px;
    background: #047857;
    color: white;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
  }

</style>

<div class="ai-canvas">
<h1>AI Diagnostic Dashboard</h1>
  <p>Real-time system health and analytics overview for offline nodes.</p>
  
  <div class="dashboard-grid">
    <div class="card">
      <h3>Local LLM Status</h3>
      <p><strong>Model:</strong> Qwen 3.5 <span class="status-badge">ONLINE</span></p>
      <p><strong>Environment:</strong> Local / Offline</p>
      <p><strong>Latency:</strong> 45ms</p>
    </div>
    
    <div class="card">
      <h3>Knowledge Base</h3>
      <p><strong>Entities Loaded:</strong> 14,500</p>
      <p><strong>Primary Source:</strong> Charaka Samhita Database</p>
      <p><strong>Sync Status:</strong> <span class="status-badge">VERIFIED</span></p>
    </div>
  </div>
</div>
