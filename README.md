# elo_balancer
proof of concept

Install indexed.py from pipi using:

```
pip install indexed.py
```

Add this function to the IndexedOrderedDict class:

```python
def move_to(self, key, idx):
        """
        Move an existing element to the a certain index.

        Raises KeyError if the element does not exist.
        """
        self._map.remove(key)
        self._map.insert(idx, key)
```
