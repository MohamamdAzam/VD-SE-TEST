from typing import List, Dict, Callable, Any

def aggregate_data(data: List[Dict[str, Any]], key: str, aggregator: Callable) -> Dict[str, Any]:
    aggregated_result = {}

    for item in data:
        group_key = item.get(key)
        value = item.get('value')  

        if group_key is not None and value is not None:
            if group_key not in aggregated_result:
                aggregated_result[group_key] = []
            aggregated_result[group_key].append(value)

    for group_key, values in aggregated_result.items():
        aggregated_result[group_key] = aggregator(values)

    return aggregated_result

# Example :
if __name__ == "__main__":
    data = [
        {'category': 'A', 'value': 10},
        {'category': 'B', 'value': 20},
        {'category': 'A', 'value': 15},
        {'category': 'B', 'value': 25},
        {'category': 'C', 'value': 30}
    ]

    def sum_values(values: List[int]) -> int:
        return sum(values)

    result = aggregate_data(data, 'category', sum_values)
    print(result) 
