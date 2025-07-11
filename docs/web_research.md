# Web Research & Search Documentation

## Overview

The Blackbird SDK includes comprehensive web research capabilities with DuckDuckGo search integration, web scraping, content processing, and intelligent research workflows.

## Core Search Features

### Basic Web Search

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.utils.web_search import WebSearchBackend
from blackbird_sdk.web_research_pipeline.enhanced_search_manager import EnhancedSearchManager
# Initialize SDK with web search capabilitiessdk = BlackbirdSDK(development_mode=True)
sdk.initialize_agent("research")
# Initialize web search backendweb_search = WebSearchBackend()
# Basic search functionalitysearch_results = web_search.search(
    query="artificial intelligence trends 2024",
    max_results=10)
print(f"Found {len(search_results)} results:")
for i, result in enumerate(search_results, 1):
    print(f"{i}. {result.get('title', 'No title')}")
    print(f"   URL: {result.get('url', 'No URL')}")
    print(f"   Snippet: {result.get('snippet', 'No snippet')[:100]}...")
    print()
```

### Agent-Integrated Search

```python
# Search with agent processingdef search_with_agent(query, agent_type="research"):
    """Search and process results with AI agent."""    sdk.initialize_agent(agent_type)
    # Perform search    search_results = web_search.search(query, max_results=5)
    # Process results with agent    search_summary = "\n".join([
        f"Title: {result.get('title', 'No title')}\n"        f"URL: {result.get('url', 'No URL')}\n"        f"Content: {result.get('snippet', 'No snippet')}\n"        for result in search_results
    ])
    analysis_prompt = f"""    Please analyze these search results for the query: "{query}"    Search Results:    {search_summary}    Provide:    1. Summary of key findings    2. Main themes and trends    3. Most reliable sources    4. Additional research recommendations    """    response = sdk.send_message(analysis_prompt)
    return {
        'query': query,
        'raw_results': search_results,
        'agent_analysis': response
    }
# Usageresearch_result = search_with_agent("quantum computing breakthroughs 2024")
print("Agent Analysis:")
print(research_result['agent_analysis'])
```

## Advanced Web Research

### Enhanced Search Manager

```python
# Initialize enhanced search managersearch_manager = EnhancedSearchManager()
# Configure search parameterssearch_config = {
    'max_results_per_source': 5,
    'enable_content_extraction': True,
    'filter_duplicates': True,
    'quality_threshold': 0.7}
# Comprehensive research queryresearch_query = "renewable energy storage solutions market analysis"# Perform enhanced searchenhanced_results = search_manager.comprehensive_search(
    query=research_query,
    config=search_config
)
print(f"Enhanced search found {len(enhanced_results)} high-quality results")
for result in enhanced_results:
    print(f"Title: {result['title']}")
    print(f"Source: {result['source']}")
    print(f"Quality Score: {result.get('quality_score', 'N/A')}")
    print(f"Content Preview: {result['content'][:200]}...")
    print("---")
```

### Multi-Source Research

```python
class MultiSourceResearcher:
    def __init__(self, sdk):
        self.sdk = sdk
        self.search_manager = EnhancedSearchManager()
    def research_topic(self, topic, search_depth="medium"):
        """Conduct comprehensive research on a topic."""        print(f"🔍 Researching: {topic}")
        # Define search strategies based on depth        search_strategies = {
            "basic": {
                "queries": [topic],
                "max_results": 10            },
            "medium": {
                "queries": [
                    topic,
                    f"{topic} latest developments",
                    f"{topic} market analysis",
                    f"{topic} future trends"                ],
                "max_results": 20            },
            "deep": {
                "queries": [
                    topic,
                    f"{topic} comprehensive analysis",
                    f"{topic} expert opinions",
                    f"{topic} case studies",
                    f"{topic} research papers",
                    f"{topic} industry reports"                ],
                "max_results": 50            }
        }
        strategy = search_strategies.get(search_depth, search_strategies["medium"])
        all_results = []
        # Execute searches        for query in strategy["queries"]:
            print(f"  Searching: {query}")
            results = self.search_manager.search(
                query=query,
                max_results=strategy["max_results"] // len(strategy["queries"])
            )
            all_results.extend(results)
        # Remove duplicates and filter quality        unique_results = self._deduplicate_results(all_results)
        quality_results = self._filter_by_quality(unique_results)
        # Analyze with AI agent        self.sdk.initialize_agent("research")
        analysis = self._analyze_results(topic, quality_results)
        return {
            'topic': topic,
            'search_depth': search_depth,
            'total_sources': len(quality_results),
            'raw_results': quality_results,
            'analysis': analysis
        }
    def _deduplicate_results(self, results):
        """Remove duplicate results."""        seen_urls = set()
        unique_results = []
        for result in results:
            url = result.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_results.append(result)
        return unique_results
    def _filter_by_quality(self, results, min_quality=0.6):
        """Filter results by quality score."""        return [
            result for result in results
            if result.get('quality_score', 0.5) >= min_quality
        ]
    def _analyze_results(self, topic, results):
        """Analyze search results with AI agent."""        results_summary = "\n\n".join([
            f"Source {i+1}:\n"            f"Title: {result.get('title', 'No title')}\n"            f"URL: {result.get('url', 'No URL')}\n"            f"Content: {result.get('content', result.get('snippet', 'No content'))[:300]}..."            for i, result in enumerate(results[:10])  # Limit to top 10 for analysis        ])
        analysis_prompt = f"""        Please provide a comprehensive analysis of this research on "{topic}".        Based on the following sources:        {results_summary}        Provide:        1. Executive Summary (3-4 sentences)        2. Key Findings (bullet points)        3. Current Trends and Developments        4. Market Analysis (if applicable)        5. Future Outlook        6. Source Quality Assessment        7. Research Gaps Identified        8. Recommendations for Further Research        Ensure the analysis is objective and cite specific sources where relevant.        """        return self.sdk.send_message(analysis_prompt)
# Usageresearcher = MultiSourceResearcher(sdk)
# Conduct research with different depthsbasic_research = researcher.research_topic("electric vehicle batteries", "basic")
print("Basic Research Results:")
print(basic_research['analysis'][:500] + "...")
deep_research = researcher.research_topic("artificial intelligence in healthcare", "deep")
print("\nDeep Research Results:")
print(deep_research['analysis'][:500] + "...")
```

## Specialized Search Features

### News and Current Events

```python
def search_latest_news(topic, time_filter="week"):
    """Search for latest news on a topic."""    time_filters = {
        "day": "past 24 hours",
        "week": "past week",
        "month": "past month"    }
    news_query = f"{topic} news {time_filters.get(time_filter, 'recent')}"    # Search for news    news_results = web_search.get_latest_news(
        topic=topic,
        max_results=10    )
    # Process with agent    sdk.initialize_agent("research")
    news_summary = "\n".join([
        f"Headline: {article.get('title', 'No title')}\n"        f"Source: {article.get('source', 'Unknown')}\n"        f"Published: {article.get('published_date', 'Unknown')}\n"        f"Summary: {article.get('summary', article.get('snippet', 'No summary'))}\n"        for article in news_results
    ])
    news_analysis = sdk.send_message(f"""    Please analyze these recent news articles about "{topic}":    {news_summary}    Provide:    1. Key developments and breaking news    2. Impact analysis    3. Trend identification    4. Credibility assessment of sources    5. Implications and next steps to watch    """)
    return {
        'topic': topic,
        'time_filter': time_filter,
        'articles': news_results,
        'analysis': news_analysis
    }
# Usagenews_analysis = search_latest_news("artificial intelligence regulation", "week")
print("Latest AI Regulation News:")
print(news_analysis['analysis'])
```

### Academic and Research Sources

```python
def search_academic_sources(topic, source_types=None):
    """Search for academic and research sources."""    if source_types is None:
        source_types = ['research papers', 'academic studies', 'peer reviewed']
    academic_queries = [
        f"{topic} {source_type}" for source_type in source_types
    ]
    # Add site-specific searches for academic sources    academic_sites = [
        "site:arxiv.org",
        "site:scholar.google.com",
        "site:pubmed.ncbi.nlm.nih.gov",
        "site:ieee.org",
        "site:acm.org"    ]
    all_results = []
    for query in academic_queries:
        # General academic search        results = web_search.search(f"{query} academic research", max_results=5)
        all_results.extend(results)
        # Site-specific searches        for site in academic_sites:
            site_results = web_search.search(f"{query} {site}", max_results=2)
            all_results.extend(site_results)
    # Filter and analyze academic sources    sdk.initialize_agent("research")
    academic_analysis = sdk.send_message(f"""    Please analyze these academic sources on "{topic}":    {json.dumps([{
        'title': r.get('title', ''),
        'url': r.get('url', ''),
        'snippet': r.get('snippet', '')
    } for r in all_results[:15]], indent=2)}    Provide:    1. Quality and credibility assessment    2. Key research findings    3. Methodology analysis    4. Research gaps identified    5. Consensus vs. conflicting findings    6. Recommendations for practitioners    """)
    return {
        'topic': topic,
        'academic_sources': all_results,
        'analysis': academic_analysis
    }
# Usageacademic_research = search_academic_sources("machine learning bias detection")
print("Academic Research Analysis:")
print(academic_research['analysis'])
```

## Web Content Processing

### Content Extraction and Analysis

```python
from blackbird_sdk.utils.web_scraper import WebScraper
class WebContentProcessor:
    def __init__(self, sdk):
        self.sdk = sdk
        self.scraper = WebScraper()
    def extract_and_analyze_content(self, urls, analysis_type="summary"):
        """Extract content from URLs and analyze."""        extracted_content = []
        for url in urls:
            try:
                print(f"Extracting content from: {url}")
                content = self.scraper.extract_content(url)
                extracted_content.append({
                    'url': url,
                    'title': content.get('title', 'No title'),
                    'content': content.get('content', ''),
                    'metadata': content.get('metadata', {})
                })
            except Exception as e:
                print(f"Failed to extract from {url}: {e}")
        # Analyze content with agent        self.sdk.initialize_agent("research")
        analysis_prompts = {
            "summary": "Provide a comprehensive summary of the key points from all sources.",
            "comparison": "Compare and contrast the different perspectives and findings.",
            "synthesis": "Synthesize the information into key insights and conclusions.",
            "fact_check": "Identify factual claims and assess their credibility."        }
        prompt = analysis_prompts.get(analysis_type, analysis_prompts["summary"])
        content_text = "\n\n".join([
            f"Source: {item['title']}\nURL: {item['url']}\n{item['content'][:1000]}..."            for item in extracted_content
        ])
        analysis = self.sdk.send_message(f"""        {prompt}        Source Content:        {content_text}        """)
        return {
            'urls': urls,
            'extracted_content': extracted_content,
            'analysis_type': analysis_type,
            'analysis': analysis
        }
# Usageprocessor = WebContentProcessor(sdk)
urls = [
    "https://example.com/ai-trends-2024",
    "https://example.com/machine-learning-advances",
    "https://example.com/ai-ethics-guidelines"]
content_analysis = processor.extract_and_analyze_content(
    urls,
    analysis_type="synthesis")
print("Content Synthesis:")
print(content_analysis['analysis'])
```

### Automated Research Workflows

```python
class AutomatedResearcher:
    def __init__(self, sdk):
        self.sdk = sdk
        self.search_manager = EnhancedSearchManager()
        self.content_processor = WebContentProcessor(sdk)
    def comprehensive_research_workflow(self, topic, output_format="report"):
        """Execute a comprehensive research workflow."""        print(f"🔬 Starting comprehensive research on: {topic}")
        workflow_steps = []
        # Step 1: Initial search and overview        print("Step 1: Initial topic search...")
        initial_search = self.search_manager.search(topic, max_results=10)
        workflow_steps.append(("initial_search", initial_search))
        # Step 2: News and current developments        print("Step 2: Current news and developments...")
        news_results = search_latest_news(topic, "month")
        workflow_steps.append(("news_analysis", news_results))
        # Step 3: Academic and research sources        print("Step 3: Academic sources...")
        academic_results = search_academic_sources(topic)
        workflow_steps.append(("academic_research", academic_results))
        # Step 4: Deep content analysis        print("Step 4: Deep content analysis...")
        top_urls = [result.get('url') for result in initial_search[:5] if result.get('url')]
        content_analysis = self.content_processor.extract_and_analyze_content(
            top_urls,
            "synthesis"        )
        workflow_steps.append(("content_analysis", content_analysis))
        # Step 5: Final synthesis        print("Step 5: Final synthesis...")
        final_report = self._generate_final_report(topic, workflow_steps, output_format)
        return {
            'topic': topic,
            'workflow_steps': workflow_steps,
            'final_report': final_report,
            'metadata': {
                'total_sources': len(initial_search) + len(news_results.get('articles', [])) + len(academic_results.get('academic_sources', [])),
                'research_date': time.time(),
                'output_format': output_format
            }
        }
    def _generate_final_report(self, topic, workflow_steps, output_format):
        """Generate final research report."""        self.sdk.initialize_agent("research")
        # Compile all analyses        all_analyses = []
        for step_name, step_data in workflow_steps:
            if isinstance(step_data, dict) and 'analysis' in step_data:
                all_analyses.append(f"{step_name.upper()}:\n{step_data['analysis']}")
        combined_analysis = "\n\n".join(all_analyses)
        format_instructions = {
            "report": "Generate a comprehensive research report with executive summary, detailed findings, and recommendations.",
            "briefing": "Create a concise executive briefing with key points and actionable insights.",
            "presentation": "Structure as presentation slides with main points and supporting data.",
            "summary": "Provide a clear, accessible summary for general audiences."        }
        format_instruction = format_instructions.get(output_format, format_instructions["report"])
        final_prompt = f"""        Based on comprehensive research on "{topic}", {format_instruction}        Research Data:        {combined_analysis}        Structure your response appropriately for the {output_format} format.        Include citations and source references where applicable.        """        return self.sdk.send_message(final_prompt)
# Usageautomated_researcher = AutomatedResearcher(sdk)
# Execute comprehensive research workflowresearch_results = automated_researcher.comprehensive_research_workflow(
    "sustainable energy transition challenges",
    output_format="report")
print("Comprehensive Research Report:")
print(research_results['final_report'])
# Save resultswith open(f"research_report_{int(time.time())}.txt", "w") as f:
    f.write(research_results['final_report'])
print("Research report saved to file.")
```

## Integration with Agents

### Search-Enhanced Agents

```python
# Create agent with web search capabilitiesfrom blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability
def create_web_search_function():
    """Create custom web search function for agents."""    def web_search_tool(query: str, max_results: int = 5) -> dict:
        """Search the web and return results."""        search_backend = WebSearchBackend()
        results = search_backend.search(query, max_results=max_results)
        return {
            'query': query,
            'results_count': len(results),
            'results': results[:max_results]
        }
    return web_search_tool
# Create research agent with web searchresearch_agent = (create_agent("web_researcher", "AI agent with web search capabilities")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""        You are a research specialist with access to web search capabilities.        You can search the internet for current information using the web_search_tool function.        When users ask for current information, use the search tool to find up-to-date data.        Always cite your sources and indicate when information comes from web searches.    """)
    .with_capabilities([
        AgentCapability.WEB_SEARCH,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.DOCUMENT_CREATION
    ])
    .with_functions([create_web_search_function()])
    .temperature(0.4)
    .build(sdk)
)
# Deploy and testsdk.deploy_custom_agent(research_agent)
# Test web search integrationresponse = sdk.send_message_to_custom_agent(
    "web_researcher",
    "What are the latest developments in quantum computing? Please search for current information.")
print("Web-Enhanced Agent Response:")
print(response)
```
