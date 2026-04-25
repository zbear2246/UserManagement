import argparse
import uvicorn

def flags():
    parser = argparse.ArgumentParser(description="web app")

    parser.add_argument(
        '-H', '--host',
        type=str,
        help="Chose a valid host",
        default='localhost'
    )

    parser.add_argument(
        '-p', '--port',
        help="chose an available port",
        type=int,
        default=8000
    )

    parser.add_argument(
        '-r', "--reload",
        type=bool,
        default=False
    )

    parser.add_argument(
        '-w', '--workers',
        type=int,
        help="number of threads uvicorn can use"
    )


    args = parser.parse_args()

    host = args.host
    port = args.port
    reload = args.reload
    
    return host, port, reload

if __name__=='__main__':
    try:
        host, port, reload = flags()

        

        uvicorn.run(
            "App.Api.WebApp:app",
            host=host,
            port=port,
            reload=reload,
            workers=4,
            limit_concurrency=100,
            timeout_keep_alive=5
        )

    except Exception as e:
        print(e)
