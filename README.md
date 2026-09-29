# LLMTesting

Repository scaffold for simple LLM test cases (designed to run against Fortiner models or any compatible LLM).

Structure:

- Golens/: Golden test cases (prompts + expected outputs)
- Evaluations/: Evaluation runner and helpers
- Context/: Context documents to include with prompts
- Report/: Report templates and output results

Quickstart (mock run):

```bash
cd /Users/venkatasaisandeepogirala/LLMTesting
python3 run_tests.py --mock
```

To run against a real model, implement `call_model` in `Evaluations/evaluate.py` to call your Fortiner model API.
