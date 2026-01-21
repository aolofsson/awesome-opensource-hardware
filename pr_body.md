## Summary
Adds four AI-powered hardware design tools to the AI section:

### Projects Added

| Project | Description | License |
|---------|-------------|---------|
| [OhmAI](https://github.com/tusharpathaknyu/OhmAI) | AI-powered SPICE circuit generation with real-time ngspice validation | MIT |
| [PCB-Thermal-AI](https://github.com/tusharpathaknyu/PCB-Thermal-AI) | ML-based PCB temperature prediction from layout features | MIT |
| [PowerElecLLM](https://github.com/tusharpathaknyu/PowerElecLLM) | Benchmark & evaluation framework for LLMs on power electronics (650 problems, ngspice validation) | MIT |
| [UVMForge](https://github.com/tusharpathaknyu/UVMForge) | LLM-powered UVM testbench generator from natural language specifications | MIT |

### Checklist
- [x] Link to source code repository
- [x] Open source projects (MIT License)
- [x] Working projects (all have live demos)
- [x] One tag line sentence per project
- [x] Alphabetically ordered within AI section

### Live Demos
Three projects have working demos deployed on Google Cloud Run:
- OhmAI: https://ohmai-761803298484.us-central1.run.app/
- PCB-Thermal-AI: https://pcb-thermal-ai-761803298484.us-central1.run.app/
- UVMForge: https://uvmforge-761803298484.us-central1.run.app/

### Benchmarks
- **PowerElecLLM**: 650 hand-crafted power electronics problems with ngspice validation. Evaluated GPT-4o (25% Pass@1), LLaMA 3.3 70B (2.3% Pass@1). Includes fine-tuning pipeline.
