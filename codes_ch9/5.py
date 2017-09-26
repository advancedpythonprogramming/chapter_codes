# 5.py

template = """
public class {0} 
{{
       public static void main(String[] args) 
       {{
           System.out.println({1});
       }} 
}}"""

print(template.format("MyClass", "'hello world'"));
