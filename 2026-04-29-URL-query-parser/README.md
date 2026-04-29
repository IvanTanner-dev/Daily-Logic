# URL Query Parser

## Lightbulb Moments

> [!TIP]
> **Data Pipeline Thinking**
> Visualized the problem as a sequence of transformations: URL String $\rightarrow$ Query String $\rightarrow$ Nested List $\rightarrow$ Final Dictionary.

> [!IMPORTANT]
> **Syntactic Sugar**
> Successfully applied Dictionary Comprehension to replace manual dictionary initialization and iterative assignment.

> [!IMPORTANT]
> **Structural Unpacking**
> Utilized key, value unpacking within a comprehension to avoid using magic numbers like [0] and [1], making the code self-documenting.

## The Challenge

Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

The query string begins after the "?",
each parameter is separated by "&",
each key/value pair is separated by "="

### Example

"https://example.com/search?name=Alice&age=30" should return:

{
  "name": "Alice",
  "age": "30"
}

## Limitations

My current solution assumes every URL must have a ?. If I ran parse_url_query("https://google.com"), it would crash because there is no [1] index!