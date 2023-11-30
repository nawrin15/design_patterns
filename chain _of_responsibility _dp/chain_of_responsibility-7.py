#Middleware Implementation Using Chain of Responsibility

#Step 1: Abstract Middleware Base
from abc import ABC, abstractmethod

# Section 1: Abstract Middleware Base

class Middleware(ABC):
    """Abstract Middleware class serving as the base of the chain."""
    
    @abstractmethod
    def handle_request(self, request):
        """Handle the request; must be implemented by concrete classes."""
        pass
    
#Step 2: Concrete Middleware Implementations
class AuthenticationMiddleware(Middleware):
    """Middleware responsible for user authentication."""
    
    def handle_request(self, request):
        """Handle authentication or pass to the next middleware in the chain."""
        if self.authenticate(request):
            print("Authentication middleware: Authenticated successfully")
            # Pass the request to the next middleware or handler in the chain.
            return super().handle_request(request)
        else:
            print("Authentication middleware: Authentication failed")
            # Stop the chain if authentication fails.
            return None

    def authenticate(self, request):
        """Implement authentication logic here."""
        # Return True if authentication is successful, else False.
        pass

class LoggingMiddleware(Middleware):
    """Middleware responsible for logging requests."""
    
    def handle_request(self, request):
        """Handle request logging and pass to the next middleware in the chain."""
        print("Logging middleware: Logging request")
        # Pass the request to the next middleware or handler in the chain.
        return super().handle_request(request)

class DataValidationMiddleware(Middleware):
    """Middleware responsible for data validation."""
    
    def handle_request(self, request):
        """Handle data validation or pass to the next middleware in the chain."""
        if self.validate_data(request):
            print("Data Validation middleware: Data is valid")
            # Pass the request to the next middleware or handler in the chain.
            return super().handle_request(request)
        else:
            print("Data Validation middleware: Invalid data")
            # Stop the chain if data validation fails.
            return None

    def validate_data(self, request):
        """Implement data validation logic here."""
        # Return True if data is valid, else False.
        pass

# Section 3: Request Handling Class and Client Code

# Chain class to handle the final request and manage middleware.
class Chain:
    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def handle_request(self, request):
        for middleware in self.middlewares:
            request = middleware.handle_request(request)
            if request is None:
                print("Request processing stopped.")
                break

# Client code to create and configure the middleware chain.
if __name__ == "__main__":
    # Create middleware instances.
    auth_middleware = AuthenticationMiddleware()
    logging_middleware = LoggingMiddleware()
    data_validation_middleware = DataValidationMiddleware()

    # Create the chain and add middleware.
    chain = Chain()
    chain.add_middleware(auth_middleware)
    chain.add_middleware(logging_middleware)
    chain.add_middleware(data_validation_middleware)

    # Simulate an HTTP request.
    http_request = {"user": "username", "data": "valid_data"}
    chain.handle_request(http_request)