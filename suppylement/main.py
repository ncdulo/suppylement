from suppylement import application

# Main application entry point.
# Create an Application instance and run it.

def main():
    app = application.Application()

    app.run()


# Though the pip installation will use the main() entry-point directly
# I'd like to keep this in for any users who wish to directly run
# Suppylement through the sh script, or by running this source file directly.
if __name__ == '__main__':
    main()
