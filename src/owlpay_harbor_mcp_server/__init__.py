from .server import serve

def main():
    """Search Owlpay Harbor documentation MCP server."""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="Search Owlpay Harbor documentation via MCP"
    )
    # no extra CLI 參數
    args = parser.parse_args()
    asyncio.run(serve())

if __name__ == "__main__":
    main()