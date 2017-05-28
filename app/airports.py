import csv
import io

class Airports(object):
  """An interface for reading data about airports."""

  def __init__(self):
    with open('third_party/airports.csv', 'r') as f:
      self.airport_file = io.StringIO(f.read())
      self.airport_reader = csv.DictReader(self.airport_file)

  def get_airport_by_iata(self, iata_code):
    """Given an IATA code, look up that airport's name.

    Args:
      iata_code: (string) The IATA code of the airport to find.

    Returns:
      string: The airport name, if found.
      None: The airport was not found.
    """
    self.airport_file.seek(0)
    for row in self.airport_reader:
      if row['iata_code'] == iata_code:
        return row['name']
    return None
