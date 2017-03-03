import engine
from ecosystem.Loop import Loop

if __name__ == "__main__":
    main_loop = Loop()
    engine.main(main_loop.loop, 15)
