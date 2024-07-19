class SpecMapper:
    def __init__(self):
        # Initialization code for SpecMapper
        pass

    def map_spec(self, spec):
        # Method to map a specification
        print(f'Mapping spec in SpecMapper: {spec}')


class CoreNormalizer(SpecMapper):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (SpecMapper)
        # Additional initialization code for CoreNormalizer

    def normalize(self, data):
        # Method to normalize data
        print(f'Normalizing data in CoreNormalizer: {data}')

    # Optionally override methods from the parent class
    def map_spec(self, spec):
        # Custom implementation for mapping a specification
        print(f'Mapping spec in CoreNormalizer: {spec}')


# Example usage
normalizer = CoreNormalizer()
normalizer.map_spec({'key': 'value'})  # Output: Mapping spec in CoreNormalizer: {'key': 'value'}
normalizer.normalize({'data': 'example'})  # Output: Normalizing data in CoreNormalizer: {'data': 'example'}
