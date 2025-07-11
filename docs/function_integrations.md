# Function Integrations Documentation

## Overview

The Blackbird SDK provides a comprehensive function calling system that enables agents to interact with external tools, APIs, and services automatically based on user queries.

## Core Integration Features

### Calculator Integration

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.integrations.calculator import Calculator
# Initialize SDK and calculatorsdk = BlackbirdSDK(development_mode=True)
calculator = Calculator()
# Initialize finance agent (which has calculator integration)sdk.initialize_agent("finance")
# Test basic calculationstest_calculations = [
    "15 + 25 * 2",
    "sqrt(144)",
    "sin(pi/2)",
    "log(100)",
    "2^8",
    "factorial(5)"]
print("🧮 Testing Calculator Functions:")
for expression in test_calculations:
    try:
        result = calculator.calculate(expression)
        print(f"✅ {expression} = {result}")
    except Exception as e:
        print(f"❌ {expression} failed: {e}")
```

### Advanced Financial Calculations

```python
class FinancialCalculator:
    def __init__(self):
        self.calculator = Calculator()
    def compound_interest(self, principal, rate, years, compounds_per_year=1):
        """Calculate compound interest."""        expression = f"{principal} * (1 + {rate/100}/{compounds_per_year})^({compounds_per_year}*{years})"        final_amount = self.calculator.calculate(expression)
        interest_earned = final_amount - principal
        return {
            "principal": principal,
            "rate": rate,
            "years": years,
            "compounds_per_year": compounds_per_year,
            "final_amount": round(final_amount, 2),
            "interest_earned": round(interest_earned, 2),
            "total_return_percentage": round((interest_earned / principal) * 100, 2)
        }
    def loan_payment(self, principal, annual_rate, years):
        """Calculate monthly loan payment."""        monthly_rate = annual_rate / 100 / 12        num_payments = years * 12        if monthly_rate == 0:
            return principal / num_payments
        expression = f"{principal} * ({monthly_rate} * (1 + {monthly_rate})^{num_payments}) / ((1 + {monthly_rate})^{num_payments} - 1)"        monthly_payment = self.calculator.calculate(expression)
        return {
            "loan_amount": principal,
            "annual_rate": annual_rate,
            "loan_term_years": years,
            "monthly_payment": round(monthly_payment, 2),
            "total_payments": round(monthly_payment * num_payments, 2),
            "total_interest": round(monthly_payment * num_payments - principal, 2)
        }
# Usage with agent integrationfin_calc = FinancialCalculator()
# Test with finance agentsdk.initialize_agent("finance")
# Agent will automatically use calculator for financial queriesresponse = sdk.send_message("""I have $10,000 to invest. If I can get 7% annual return compounded monthly,what will it be worth in 10 years? Please calculate: 10000 * (1.07/12)^(12*10)""")
print("Finance Agent with Calculator:")
print(response)
```

### Calendar Integration

```python
from blackbird_sdk.integrations.calendar import CalendarManager
from datetime import datetime, timedelta
# Initialize calendar managercalendar = CalendarManager()
# Test calendar operationsdef test_calendar_functions():
    """Test calendar integration functions."""    current_date = datetime.now()
    print(f"📅 Current date: {current_date.strftime('%Y-%m-%d %H:%M')}")
    # Calculate future dates    future_date = current_date + timedelta(days=90)
    print(f"📅 Date in 90 days: {future_date.strftime('%Y-%m-%d')}")
    # Calculate business days    business_days = calendar.calculate_business_days(
        start_date=current_date,
        end_date=future_date
    )
    print(f"📊 Business days in next 90 days: {business_days}")
    # Working days calculation    working_days = calendar.get_working_days_between(
        start_date=current_date.date(),
        end_date=future_date.date()
    )
    print(f"💼 Working days: {working_days}")
test_calendar_functions()
```

### Agent-Integrated Calendar Usage

```python
# Test calendar integration with agentsdk.initialize_agent("finance")
calendar_queries = [
    "I need to plan my quarterly financial review. Today is the start date, and I want to schedule it for 90 days from now. What date would that be?",
    "How many business days do I have to prepare for a presentation in 30 days?",
    "If I start a project today and need to complete it in 6 months, what's the deadline date?",
    "Calculate the number of working days between now and the end of this year."]
print("📅 Testing Calendar Integration with Finance Agent:")
for query in calendar_queries:
    print(f"\nQuery: {query}")
    response = sdk.send_message(query)
    print(f"Response: {response}")
```

## Custom Function Creation

### Building Custom Functions

```python
def create_investment_analyzer():
    """Create custom investment analysis functions."""    def analyze_portfolio_risk(allocations: dict, risk_factors: dict = None) -> dict:
        """Analyze portfolio risk based on asset allocations."""        if risk_factors is None:
            risk_factors = {
                "stocks": 0.8,
                "bonds": 0.3,
                "cash": 0.0,
                "crypto": 1.0,
                "real_estate": 0.6,
                "commodities": 0.7            }
        total_weight = sum(allocations.values())
        if total_weight == 0:
            return {"error": "No allocations provided"}
        weighted_risk = sum(
            (weight / total_weight) * risk_factors.get(asset, 0.5)
            for asset, weight in allocations.items()
        )
        risk_level = (
            "High" if weighted_risk > 0.7 else            "Medium" if weighted_risk > 0.4 else            "Low"        )
        recommendations = []
        if weighted_risk > 0.8:
            recommendations.append("Consider reducing high-risk assets")
        if allocations.get("cash", 0) / total_weight > 0.3:
            recommendations.append("Consider investing excess cash")
        if len(allocations) < 3:
            recommendations.append("Increase diversification across asset classes")
        return {
            "overall_risk_score": round(weighted_risk, 3),
            "risk_level": risk_level,
            "asset_breakdown": allocations,
            "total_portfolio_value": total_weight,
            "recommendations": recommendations,
            "diversification_score": len(allocations) / 6.0  # Max 6 asset classes        }
    def calculate_retirement_needs(current_age: int, retirement_age: int,
                                 current_savings: float, monthly_expenses: float,
                                 inflation_rate: float = 0.03) -> dict:
        """Calculate retirement savings needs."""        years_to_retirement = retirement_age - current_age
        years_in_retirement = max(85 - retirement_age, 20)  # Assume living to 85        # Calculate future monthly expenses (adjusted for inflation)        future_monthly_expenses = monthly_expenses * ((1 + inflation_rate) ** years_to_retirement)
        # Calculate total retirement needs        total_retirement_needs = future_monthly_expenses * 12 * years_in_retirement
        # Calculate required monthly savings        if years_to_retirement > 0:
            # Assuming 7% annual return            monthly_return = 0.07 / 12            num_payments = years_to_retirement * 12            # Future value of current savings            future_current_savings = current_savings * ((1 + monthly_return) ** num_payments)
            # Additional savings needed            additional_needed = max(0, total_retirement_needs - future_current_savings)
            # Required monthly payment            if additional_needed > 0 and monthly_return > 0:
                required_monthly_savings = additional_needed * monthly_return / (((1 + monthly_return) ** num_payments) - 1)
            else:
                required_monthly_savings = 0        else:
            required_monthly_savings = 0            additional_needed = max(0, total_retirement_needs - current_savings)
        return {
            "current_age": current_age,
            "retirement_age": retirement_age,
            "years_to_retirement": years_to_retirement,
            "current_savings": current_savings,
            "current_monthly_expenses": monthly_expenses,
            "future_monthly_expenses": round(future_monthly_expenses, 2),
            "total_retirement_needs": round(total_retirement_needs, 2),
            "required_monthly_savings": round(required_monthly_savings, 2),
            "savings_gap": round(additional_needed, 2),
            "on_track": additional_needed <= current_savings * 0.1  # Within 10%        }
    return analyze_portfolio_risk, calculate_retirement_needs
# Create functionsportfolio_analyzer, retirement_calculator = create_investment_analyzer()
# Test functions directlyportfolio_test = portfolio_analyzer({
    "stocks": 6000,
    "bonds": 3000,
    "cash": 1000})
print("Portfolio Analysis:")
print(json.dumps(portfolio_test, indent=2))
retirement_test = retirement_calculator(30, 65, 50000, 4000)
print("\nRetirement Analysis:")
print(json.dumps(retirement_test, indent=2))
```

### Creating Agents with Custom Functions

```python
from blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability
# Create financial advisor agent with custom functionsfinancial_advisor = (create_agent("advanced_financial_advisor", "Advanced financial planning specialist")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""        You are an advanced financial advisor with access to specialized analysis tools:        Available Functions:        - analyze_portfolio_risk: Analyze portfolio risk and diversification        - calculate_retirement_needs: Calculate retirement savings requirements        Use these tools to provide detailed, data-driven financial advice.        Always explain your calculations and provide clear recommendations.    """)
    .with_capabilities([
        AgentCapability.CALCULATIONS,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.FILE_PROCESSING
    ])
    .with_functions([portfolio_analyzer, retirement_calculator])
    .temperature(0.3)
    .max_tokens(4000)
    .instruction("analysis_style", "Provide detailed numerical analysis with explanations")
    .instruction("recommendations", "Include specific, actionable recommendations")
    .build(sdk)
)
# Deploy and test the agentsdk.deploy_custom_agent(financial_advisor)
# Test with complex financial queriestest_queries = [
    "I'm 35 years old with $75,000 saved for retirement. I spend $5,000 per month and want to retire at 65. Am I on track?",
    "Analyze my portfolio: 70% stocks ($70,000), 20% bonds ($20,000), 10% cash ($10,000). Is this appropriate for a 40-year-old?",
    "I have a portfolio worth $100,000 split between stocks (60%), real estate (25%), and crypto (15%). What's my risk level?"]
for query in test_queries:
    print(f"\n🔍 Query: {query}")
    response = sdk.send_message_to_custom_agent("advanced_financial_advisor", query)
    print(f"💡 Response: {response}")
```

## API Integrations

### External API Function Wrapper

```python
import requests
class APIFunctionWrapper:
    """Wrapper for external API integrations."""    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers = {}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'    def create_api_function(self, endpoint, method='GET', description=""):
        """Create a function that calls an external API."""        def api_function(params=None, data=None):
            """Generated API function."""            url = f"{self.base_url}/{endpoint.lstrip('/')}"            try:
                if method.upper() == 'GET':
                    response = requests.get(url, params=params, headers=self.headers, timeout=30)
                elif method.upper() == 'POST':
                    response = requests.post(url, json=data, headers=self.headers, timeout=30)
                else:
                    raise ValueError(f"Unsupported method: {method}")
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                return {"error": f"API call failed: {str(e)}"}
        # Set function metadata        api_function.__name__ = f"api_{endpoint.replace('/', '_').replace('-', '_')}"        api_function.__doc__ = description or f"Call {endpoint} API endpoint"        return api_function
# Example: Weather API integrationweather_api = APIFunctionWrapper("https://api.weather.example.com")
get_weather = weather_api.create_api_function(
    "weather/current",
    method='GET',
    description="Get current weather for a location")
get_forecast = weather_api.create_api_function(
    "weather/forecast",
    method='GET',
    description="Get weather forecast for a location")
# Create agent with API functionsweather_agent = (create_agent("weather_assistant", "Weather information assistant")
    .personality(AgentPersonality.FRIENDLY)
    .system_prompt("""        You are a weather assistant with access to current weather and forecast data.        Use the available weather functions to provide accurate, up-to-date information.    """)
    .with_functions([get_weather, get_forecast])
    .build(sdk)
)
```

## Function Registry Management

### Advanced Function Registry

```python
from blackbird_sdk.integrations.function_registry import FunctionRegistry
class AdvancedFunctionRegistry(FunctionRegistry):
    """Enhanced function registry with categories and metadata."""    def __init__(self):
        super().__init__()
        self.function_categories = {}
        self.function_metadata = {}
    def register_function_with_metadata(self, func, category="general",
                                      description="", usage_examples=None):
        """Register function with additional metadata."""        self.register_function(func)
        func_name = func.__name__        self.function_categories[func_name] = category
        self.function_metadata[func_name] = {
            "description": description,
            "usage_examples": usage_examples or [],
            "category": category,
            "parameters": self._extract_parameters(func)
        }
    def _extract_parameters(self, func):
        """Extract function parameters using inspection."""        import inspect
        try:
            sig = inspect.signature(func)
            parameters = {}
            for name, param in sig.parameters.items():
                parameters[name] = {
                    "type": str(param.annotation) if param.annotation != inspect.Parameter.empty else "any",
                    "default": param.default if param.default != inspect.Parameter.empty else None,
                    "required": param.default == inspect.Parameter.empty
                }
            return parameters
        except Exception:
            return {}
    def get_functions_by_category(self, category):
        """Get all functions in a category."""        return [
            name for name, cat in self.function_categories.items()
            if cat == category
        ]
    def get_function_help(self, func_name):
        """Get comprehensive help for a function."""        if func_name not in self.functions:
            return None        func = self.functions[func_name]
        metadata = self.function_metadata.get(func_name, {})
        help_text = f"""Function: {func_name}Category: {metadata.get('category', 'general')}Description: {metadata.get('description', func.__doc__ or 'No description')}Parameters:"""        for param_name, param_info in metadata.get('parameters', {}).items():
            required = "required" if param_info['required'] else "optional"            default = f" (default: {param_info['default']})" if param_info['default'] is not None else ""            help_text += f"  - {param_name} ({param_info['type']}, {required}){default}\n"        if metadata.get('usage_examples'):
            help_text += "\nUsage Examples:\n"            for example in metadata['usage_examples']:
                help_text += f"  - {example}\n"        return help_text.strip()
# Usageregistry = AdvancedFunctionRegistry()
# Register functions with metadataregistry.register_function_with_metadata(
    portfolio_analyzer,
    category="finance",
    description="Analyze portfolio risk and asset allocation",
    usage_examples=[
        "analyze_portfolio_risk({'stocks': 7000, 'bonds': 3000})",
        "analyze_portfolio_risk({'stocks': 5000, 'bonds': 3000, 'cash': 2000})"    ]
)
registry.register_function_with_metadata(
    retirement_calculator,
    category="finance",
    description="Calculate retirement savings requirements",
    usage_examples=[
        "calculate_retirement_needs(30, 65, 50000, 4000)",
        "calculate_retirement_needs(25, 60, 25000, 3500, 0.025)"    ]
)
# Get help for functionsprint("Function Help:")
print(registry.get_function_help("analyze_portfolio_risk"))
```

## Automatic Function Selection

### Smart Function Calling

```python
class SmartFunctionCaller:
    """Intelligent function selection based on user queries."""    def __init__(self, sdk, function_registry):
        self.sdk = sdk
        self.registry = function_registry
        self.query_patterns = self._build_query_patterns()
    def _build_query_patterns(self):
        """Build patterns to match queries to functions."""        return {
            "calculate": ["calculator", "math", "arithmetic"],
            "date": ["calendar", "time", "schedule", "when"],
            "risk": ["portfolio_analyzer", "investment", "allocation"],
            "retirement": ["retirement_calculator", "savings", "pension"],
            "weather": ["weather", "forecast", "temperature"],
            "portfolio": ["portfolio_analyzer", "diversification", "assets"]
        }
    def analyze_query_intent(self, query):
        """Analyze query to determine appropriate functions."""        query_lower = query.lower()
        potential_functions = []
        # Check for calculation needs        calc_keywords = ["calculate", "compute", "+", "-", "*", "/", "^", "sqrt", "sin", "cos"]
        if any(keyword in query_lower for keyword in calc_keywords):
            potential_functions.append("calculator")
        # Check for date/time needs        date_keywords = ["date", "when", "calendar", "schedule", "days", "weeks", "months"]
        if any(keyword in query_lower for keyword in date_keywords):
            potential_functions.append("calendar")
        # Check for financial analysis needs        finance_keywords = ["portfolio", "investment", "risk", "allocation", "stocks", "bonds"]
        if any(keyword in query_lower for keyword in finance_keywords):
            potential_functions.append("portfolio_analyzer")
        # Check for retirement planning        retirement_keywords = ["retirement", "retire", "pension", "savings goal"]
        if any(keyword in query_lower for keyword in retirement_keywords):
            potential_functions.append("retirement_calculator")
        return potential_functions
    def execute_smart_query(self, query):
        """Execute query with automatic function selection."""        # Analyze query intent        suggested_functions = self.analyze_query_intent(query)
        if not suggested_functions:
            # No specific functions needed, use regular agent            return self.sdk.send_message(query)
        # Build context about available functions        function_context = "Available functions for this query:\n"        for func_name in suggested_functions:
            if func_name in ["calculator", "calendar"]:
                function_context += f"- {func_name}: Built-in {func_name} capabilities\n"            else:
                help_text = self.registry.get_function_help(func_name)
                if help_text:
                    function_context += f"- {func_name}: {help_text.split('Description:')[^1].split('Parameters:')[^0].strip()}\n"        # Enhanced query with function awareness        enhanced_query = f"""{function_context}User Query: {query}Please use the appropriate functions to answer this query accurately."""        return self.sdk.send_message(enhanced_query)
# Usagesmart_caller = SmartFunctionCaller(sdk, registry)
# Test smart function callingtest_queries = [
    "What's 15% of $50,000?",
    "How many business days until Christmas?",
    "I have $60,000 in stocks and $20,000 in bonds. What's my portfolio risk?",
    "I'm 28, want to retire at 62, have $30,000 saved, and spend $3,800/month. Am I on track?"]
print("🤖 Smart Function Calling Tests:")
for query in test_queries:
    print(f"\nQuery: {query}")
    suggested = smart_caller.analyze_query_intent(query)
    print(f"Suggested functions: {suggested}")
    response = smart_caller.execute_smart_query(query)
    print(f"Response: {response[:200]}...")
```

## Function Integration Best Practices

### Error Handling and Validation

```python
class RobustFunctionWrapper:
    """Wrapper for robust function execution with error handling."""    @staticmethod    def validate_and_execute(func, *args, **kwargs):
        """Execute function with validation and error handling."""        try:
            # Validate inputs            validated_args = []
            for arg in args:
                if isinstance(arg, str) and arg.replace('.', '').replace('-', '').isdigit():
                    validated_args.append(float(arg))
                else:
                    validated_args.append(arg)
            # Execute function            result = func(*validated_args, **kwargs)
            # Validate output            if isinstance(result, dict) and 'error' in result:
                return {"success": False, "error": result['error']}
            return {"success": True, "result": result}
        except Exception as e:
            return {"success": False, "error": f"Function execution failed: {str(e)}"}
# Example usagedef safe_portfolio_analysis(allocations_dict):
    """Safe wrapper for portfolio analysis."""    try:
        allocations = {}
        if isinstance(allocations_dict, str):
            # Parse string representation            import ast
            allocations = ast.literal_eval(allocations_dict)
        else:
            allocations = allocations_dict
        return RobustFunctionWrapper.validate_and_execute(
            portfolio_analyzer,
            allocations
        )
    except Exception as e:
        return {"success": False, "error": f"Invalid input: {e}"}
# Test error handlingtest_result = safe_portfolio_analysis("{'stocks': 7000, 'bonds': 3000}")
print("Safe execution result:")
print(json.dumps(test_result, indent=2))
```

This comprehensive function integration system enables your Blackbird SDK to automatically handle calculations, calendar operations, and complex financial analyses based on user queries, providing a seamless and intelligent user experience.
