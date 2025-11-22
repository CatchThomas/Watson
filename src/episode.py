"""Episode runner that orchestrates agent, environment, and reward."""
from typing import Dict, Any
from src.agent import AgentLLM
from src.environment import EnvironmentLLM
from src.reward import RewardLLM
from src.scenarios import AttackScenario


class EpisodeRunner:
    """
    Runs a single episode: agent investigates, environment responds, reward is calculated.
    """
    
    def __init__(self):
        """Initialize the episode runner."""
        self.agent = AgentLLM(max_tool_calls=100)
        self.reward_llm = RewardLLM()
    
    def run_episode(self, scenario: AttackScenario) -> Dict[str, Any]:
        """
        Run a single episode with a given scenario.
        
        Args:
            scenario: The attack scenario to investigate
            
        Returns:
            Dictionary containing episode results including reward
        """
        # Initialize environment for this scenario
        environment = EnvironmentLLM(scenario)
        
        # Define query callback that uses the environment
        def query_callback(query: str) -> str:
            return environment.query(query, context=environment.conversation_history)
        
        # Run agent investigation
        investigation_result = self.agent.investigate(
            scenario_description=scenario.description,
            query_callback=query_callback
        )
        
        # Calculate reward
        reward_result = self.reward_llm.calculate_reward(
            scenario=scenario,
            agent_investigation=investigation_result,
            tool_calls_made=investigation_result["tool_calls_made"]
        )
        
        return {
            "scenario_id": scenario.id,
            "scenario_name": scenario.name,
            "investigation": investigation_result,
            "reward": reward_result,
        }

