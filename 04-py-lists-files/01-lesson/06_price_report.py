from pathlib import Path

# ".." betyr å gå en mappe utover
# / setter sammen flere mapper og filnavn
data_directory = Path("..") / "data"
prices_path = data_directory / "prices.txt"
report_path = data_directory / "report_path.txt"
prices = []

with open(prices_path, "r", encoding="utf-8") as file:
    for line in file:
        prices.append(float(line.strip()))

print(prices)

print("\n---\n")

average = sum(prices) / len(prices)

with open(report_path, "w", encoding="utf-8") as file:
    file.write(f"Count: {len(prices)}\n")
    file.write(f"Sum: {sum(prices):.2f}\n")
    file.write(f"Average: {average:.2f}\n")




