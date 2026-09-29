#!/usr/bin/env python3
import os
import json
import argparse

def call_model(prompt, expected=None):
    """Placeholder for calling a Fortiner model.
    If `LLM_TEST_MOCK` env var is set to '1', return `expected` (mock pass).
    Otherwise raise NotImplementedError to prompt user implementation.
    """
    if os.getenv("LLM_TEST_MOCK") == "1":
        return expected if expected is not None else "MOCK_RESPONSE"
    raise NotImplementedError(
        "Implement `call_model(prompt)` to call your Fortiner model API or set LLM_TEST_MOCK=1 for local mock runs"
    )

def load_golens(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate(golens_path, report_path):
    golens = load_golens(golens_path)
    results = []
    for t in golens:
        prompt = t.get('prompt')
        expected = t.get('expected')
        try:
            output = call_model(prompt, expected=expected)
            note = None
        except Exception as e:
            output = None
            note = str(e)
        passed = False
        if output is not None and isinstance(output, str) and expected is not None:
            passed = output.strip() == expected.strip()
        status = 'pass' if passed else 'fail' if output is not None else 'error'
        results.append({
            'id': t.get('id'),
            'status': status,
            'expected': expected,
            'output': output,
            'note': note,
        })

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({'results': results}, f, indent=2, ensure_ascii=False)

    passed_count = sum(1 for r in results if r['status'] == 'pass')
    total = len(results)
    print(f"Evaluation complete: {passed_count}/{total} passed. Report saved to {report_path}")
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run LLM tests against Golens')
    parser.add_argument('--golens', default='Golens/sample_golens.json')
    parser.add_argument('--report', default='Report/results.json')
    args = parser.parse_args()
    evaluate(args.golens, args.report)
