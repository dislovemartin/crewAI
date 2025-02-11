from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools.base_tool import BaseTool
from crewai.utilities import I18N

from .ask_question_tool import AskQuestionTool
from .delegate_work_tool import DelegateWorkTool


class AgentTools:
    """Manager class for agent-related tools"""

    def __init__(self, agents: list[BaseAgent], i18n: I18N = I18N()):
        self.agents = agents
        self.i18n = i18n

    def tools(self) -> list[BaseTool]:
        """Get all available agent tools"""
        coworkers = []
        for agent in self.agents:
            coworker_desc = f"{agent.role} (Goal: {agent.goal})"
            if agent.backstory:
                # Truncate backstory to first sentence for brevity
                first_sentence = agent.backstory.split('.')[0]
                coworker_desc += f" - {first_sentence}"
            coworkers.append(coworker_desc)
        
        coworkers_str = "\n- ".join(coworkers)

        delegate_tool = DelegateWorkTool(
            agents=self.agents,
            i18n=self.i18n,
            description=self.i18n.tools("delegate_work").format(coworkers=coworkers_str),  # type: ignore
        )

        ask_tool = AskQuestionTool(
            agents=self.agents,
            i18n=self.i18n,
            description=self.i18n.tools("ask_question").format(coworkers=coworkers_str),  # type: ignore
        )

        return [delegate_tool, ask_tool]
