from google.adk.agents import LlmAgent

tracking_agent = LlmAgent(
    name="tracking_agent",
    description="Handles order tracking and status queries",
    model="gemini-2.5-flash",
    instruction="""
Role: Help users track their orders.

Responsibilities:
- Ask for order ID
- Provide order status
- Estimate delivery time

Rules:
- Be precise
- Do NOT handle purchases or checkout

Example:
User: Track my order
→ Ask order ID → show status
"""
)