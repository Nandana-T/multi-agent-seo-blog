# agents/planning_agent.py
class PlanningAgent:
    def create_outline(self, research_data):
        return f"""
# {research_data['topic']}
## Introduction
- Brief overview
- Importance in 2025

## Section 1: Current Trends
- Trend 1
- Trend 2

## Section 2: Implementation Strategies
- Strategy 1
- Strategy 2

## Section 3: Benefits and Challenges
- Benefits
- Challenges

## Conclusion
- Summary
- Call to action
"""