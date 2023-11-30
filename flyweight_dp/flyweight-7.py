"The Flyweight Use Case Example"

"The Flyweight that contains an intrinsic value called code"

class Flyweight():  # pylint: disable=too-few-public-methods
    "The Flyweight that contains an intrinsic value called code"

    def __init__(self, code: str) -> None:
        self.code = code
        
"Creating the FlyweightFactory as a singleton"

class FlyweightFactory():
    "Creating the FlyweightFactory as a singleton"

    _flyweights: dict[str, Flyweight] = {}  # Python 3.9
    # _flyweights = {}  # Python 3.8 or earlier

    def __new__(cls):
        return cls

    @classmethod
    def get_flyweight(cls, code: str) -> Flyweight:
        "A static method to get a flyweight based on a code"
        if not code in cls._flyweights:
            cls._flyweights[code] = Flyweight(code)
        return cls._flyweights[code]

    @classmethod
    def get_count(cls) -> int:
        "Return the number of flyweights in the cache"
        return len(cls._flyweights)
    
"A Column that is used in a Row"

class Column():  # pylint: disable=too-few-public-methods
    """
    The columns are the contexts.
    They will share the Flyweights via the FlyweightsFactory.
    `data`, `width` and `justify` are extrinsic values. They are outside
    of the flyweights.
    """

    def __init__(self, data="", width=11, justify=0) -> None:
        self.data = data
        self.width = width
        self.justify = justify  # 0:center, 1:left, 2:right

    def get_data(self):
        "Get the flyweight value from the factory, and apply the extrinsic values"
        ret = ""
        for data in self.data:
            ret = ret + FlyweightFactory.get_flyweight(data).code
        ret = f"{ret.center(self.width)}" if self.justify == 0 else ret
        ret = f"{ret.ljust(self.width)}" if self.justify == 1 else ret
        ret = f"{ret.rjust(self.width)}" if self.justify == 2 else ret
        return ret

"A Row in the Table"
class Row():  # pylint: disable=too-few-public-methods
    "A Row in the Table"

    def __init__(self, column_count: int) -> None:
        self.columns = []
        for _ in range(column_count):
            self.columns.append(Column())

    def get_data(self):
        "Format the row before returning it to the table"
        ret = ""
        for column in self.columns:
            ret = f"{ret}{column.get_data()}|"
        return ret
    
"A Formatted Table that includes rows and columns"
class Table():  # pylint: disable=too-few-public-methods
    "A Formatted Table"

    def __init__(self, row_count: int, column_count: int) -> None:
        self.rows = []
        for _ in range(row_count):
            self.rows.append(Row(column_count))

    def draw(self):
        "Draws the table formatted in the console"
        max_row_length = 0
        rows = []
        for row in self.rows:
            row_data = row.get_data()
            rows.append(f"|{row_data}")
            row_length = len(row_data) + 1
            if max_row_length < row_length:
                max_row_length = row_length
        print("-" * max_row_length)
        for row in rows:
            print(row)
        print("-" * max_row_length)

TABLE = Table(3, 3)

TABLE.rows[0].columns[0].data = "abra"
TABLE.rows[0].columns[1].data = "112233"
TABLE.rows[0].columns[2].data = "cadabra"
TABLE.rows[1].columns[0].data = "racadab"
TABLE.rows[1].columns[1].data = "12345"
TABLE.rows[1].columns[2].data = "332211"
TABLE.rows[2].columns[0].data = "cadabra"
TABLE.rows[2].columns[1].data = "445566"
TABLE.rows[2].columns[2].data = "aa 22 bb"

TABLE.rows[0].columns[0].justify = 1
TABLE.rows[1].columns[0].justify = 1
TABLE.rows[2].columns[0].justify = 1
TABLE.rows[0].columns[2].justify = 2
TABLE.rows[1].columns[2].justify = 2
TABLE.rows[2].columns[2].justify = 2
TABLE.rows[0].columns[1].width = 15
TABLE.rows[1].columns[1].width = 15
TABLE.rows[2].columns[1].width = 15

TABLE.draw()

print(f"FlyweightFactory has {FlyweightFactory.get_count()} flyweights")