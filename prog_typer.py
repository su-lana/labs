import typer
from typing import Optional, List
from pathlib import Path

app = typer.Typer()

@app.command()
def main(
    integers : List[int] = typer.Argument([], help = "Numbers to be summed"),
    file : Optional[Path] = typer.Option(None, "-f", help = "Path to a file containing numbers to be summed"),
    output : Optional[Path] = typer.Option(None, "-o", help = "Path to a file where the result will be saved")
):
    
    vals_to_sum = list(integers) if integers else []

    if file and file.exists():
        content = file.read_text().splitlines()
        vals_to_sum.extend(int(line.strip()) for line in content if line.strip())

    if not vals_to_sum:
        print("No input provided")
        raise typer.Exit()

    result = sum(vals_to_sum)
    print(result)

    if output:
        output.write_text(str(result))
        typer.echo(f"Result saved to {output}")
              
if __name__ == "__main__":
    app()