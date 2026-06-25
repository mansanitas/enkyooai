import pandas as pd

# 2. Create a DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
}
df = pd.DataFrame(data)
df = df.replace("Alice", "Alicia")
