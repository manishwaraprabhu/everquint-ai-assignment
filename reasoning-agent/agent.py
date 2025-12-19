from llm_client_ollama import LLMClient
import re

class ReasoningAgent:
    
    def __init__(self, model_name="phi3:mini"):
        self.llm = LLMClient(model_name=model_name)

    # STEP 1: PLANNING
    def plan_steps(self, question: str) -> str:
        prompt = f"""
Create a clear step-by-step plan to solve the problem.

Rules:
- Return numbered steps only
- Be concise
- No explanations beyond the steps

Question:
{question}
"""
        return self.llm.generate(prompt)

    # STEP 2: SOLVING (EXECUTION)
    def solve(self, question: str) -> str:
        prompt = f"""
Solve the problem step-by-step internally.

IMPORTANT RULES:
- Do NOT show intermediate reasoning
- At the end, output ONLY the final answer
- Use this EXACT format (mandatory):

FINAL ANSWER: <answer>

The answer may be:
- A number
- Text
- A time duration (e.g., 3 hours 35 minutes)
- A time range (e.g., 11:00–12:00)

Question:
{question}
"""
        return self.llm.generate(prompt)

    # STEP 3: VERIFICATION
    def verify(self, question: str, solution: str) -> str:
        prompt = f"""
Verify the solution carefully.

Validation checklist:
- Arithmetic correctness
- Time calculations are correct
- Minimum duration constraints are respected
- Logical consistency with the question
- No violation of constraints or boundaries

If ALL checks pass, respond exactly:
PASS

Otherwise respond exactly:
FAIL

Question:
{question}

Solution:
{solution}
"""
        return self.llm.generate(prompt)

    # ANSWER EXTRACTION
    def _extract_final_answer(self, text: str) -> str:
        """
        Extracts everything after 'FINAL ANSWER:' safely,
        supporting numeric, text, and time-based answers.
        """
        match = re.search(r"FINAL ANSWER:\s*(.*)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "N/A"

    # USER-FRIENDLY EXPLANATION
    def _build_user_reasoning(self, question: str, final_answer: str) -> str:
        prompt = f"""
Explain the solution in ONE concise paragraph for a user.

Rules:
- No formulas
- No step numbers
- Simple explanation

Question:
{question}

Final Answer:
{final_answer}
"""
        reasoning = self.llm.generate(prompt)
        reasoning = reasoning.replace("\\", "")
        reasoning = reasoning.replace("{", "").replace("}", "")
        return reasoning.strip()

    # FULL PIPELINE
    def run(self, question: str) -> dict:
        # Step 1: Plan
        plan_raw = self.plan_steps(question)
        plan_lines = [line.strip() for line in plan_raw.split("\n") if line.strip()]
        plan_text = "Here are the steps to solve the problem:\n\n" + "\n".join(
            [f"{i + 1}. {line}" for i, line in enumerate(plan_lines)]
        )

        # Step 2: Solve
        solution = self.solve(question)
        final_answer = self._extract_final_answer(solution)

        # Step 3: Verify
        verification = self.verify(question, solution)
        passed = "PASS" in verification.upper()

        # Step 4: User explanation
        user_reasoning = self._build_user_reasoning(question, final_answer)

        return {
            "answer": final_answer,
            "status": "success" if passed else "verification_failed",
            "reasoning_visible_to_user": user_reasoning,
            "metadata": {
                "plan": plan_text,
                "checks": [
                    {
                        "check_name": "Primary Verification",
                        "passed": passed,
                        "details": "PASS" if passed else "FAIL"
                    }
                ],
                "retries": 0
            }
        }