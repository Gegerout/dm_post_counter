# Boolean Function Classification by Post Classes
[![ru](https://img.shields.io/badge/lang-ru-green.svg)](https://github.com/Gegerout/dm_post_counter/blob/main/README.md)

This project is designed to find the number of boolean functions with `n` variables for all configurations of Post classes. The program generates all truth tables for a given number of variables and classifies them into Post classes:

- **T0**: A function that keeps 0.
- **T1**: A function that keeps 1.
- **Self-dual (S)**: A self-dual function.
- **Monotone (M)**: A monotone function.
- **Linear (L)**: A linear function.

## How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Gegerout/dm_post_counter.git
   ```

2. **Navigate to the project directory**:
    ```bash
    cd dm_post_counter
    ```
3. **Run the program**:
    ```bash
    python main.py
    ```
   
## Example of Program Output

**Example input:**

```plaintext
Enter the number of variables (n): 2
```
**Example output:**

```plaintext
Post classification and the number of functions:
+--------------------------------------+------------+
| Classification                       | Quantity   |
+--------------------------------------+------------+
| T0, M, L                             | 1          |
| Not belonging to any class           | 2          |
| T0                                   | 2          |
| S, L                                 | 2          |
| T0, L                                | 1          |
| T0, T1, M                            | 2          |
| T1, L                                | 1          |
| T0, T1, S, M, L                      | 2          |
| T1                                   | 2          |
| T1, M, L                             | 1          |
+--------------------------------------+------------+
```
