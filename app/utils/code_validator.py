import ast
import tokenize
from io import StringIO

def validate_syntax(code: str) -> bool:
    """
    Validates Python code syntax using the ast module.
    Returns True if syntax is valid, False otherwise.
    """
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def validate_style(code: str) -> dict:
    """
    Validates code style according to PEP 8 guidelines.
    Returns a dictionary with style validation results.
    """
    results = {
        "valid": True,
        "issues": []
    }
    
    try:
        # Tokenize the code to check for style issues
        tokens = tokenize.generate_tokens(StringIO(code).readline)
        
        line_length = 0
        for token in tokens:
            # Check line length
            if token.type == tokenize.NEWLINE:
                if line_length > 79:
                    results["valid"] = False
                    results["issues"].append(f"Line too long: {line_length} characters")
                line_length = 0
            else:
                line_length += len(token.string)
        
        return results
    except tokenize.TokenError:
        results["valid"] = False
        results["issues"].append("Invalid token found")
        return results
