import argparse
from app import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--processor","-p",choices=['memory','file'], default='memory')
    parser.add_argument("--debug","-d",action='store_true', default=False)
    args = parser.parse_args()
    app.config.update({'processor': args.processor,'DEBUG': args.debug})
    if args.debug:
        print(app.config)
    app.run()
