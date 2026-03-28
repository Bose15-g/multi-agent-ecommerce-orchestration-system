from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext

# Tool to save user info
def save_user_info(tool_context: ToolContext,
                   name: str,
                   email: str,
                   mobile: str):
    tool_context.state["name"] = name
    tool_context.state["email"] = email
    tool_context.state["mobile"] = mobile

# Import sub-agents
from catalog_agent.agent import catalog_agent
from checkout_agent.agent import checkout_agent
from tracking_agent.agent import tracking_agent

root_agent = LlmAgent(
    name="ecommerce_agent",
    description="Main agent that controls ecommerce workflow",
    model="gemini-2.5-flash",
    instruction="""
Role: You are an ecommerce assistant.

Workflow:
1. Greet user and explain capabilities.
2. Collect user details (name, email, mobile).
   - Ask ONE detail at a time.
   - If already available, don't ask again.
3. Once collected, call save_user_info tool.
4. Identify user intent:
   - Buying → catalog_agent
   - Checkout → checkout_agent
   - Tracking → tracking_agent

Rules:
- NEVER answer product/checkout/tracking queries yourself.
- ALWAYS delegate to exactly ONE sub-agent.
- Ask clarification if unclear.
- Pass sub-agent response directly to user.
""",
    tools=[save_user_info],
    sub_agents=[
        catalog_agent,
        checkout_agent,
        tracking_agent
    ]
)