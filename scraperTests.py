import unittest
import artveeScraper

class TestUtilities(unittest.TestCase):
    def test_fourDigitYear(self):
        testCases = [
            ("Vegetable-Analytic (1932)", ["1932"]),
            ("Gelukwens bij de geboorte van Juliana Bellaar Spruyt (1935-05-13) ", ["1935"]),
            ("Farvestudie til Langelinie-billedet (1922 - 1927) ", ["1922", "1927"]),
            ("Ontwerp voor raam in het Noordertransept in de Dom te Utrecht 58 (ca. 1878-1938)", ["1878", "1938"]),
            ("Prostitution universelle (Universal Prostitution) (1916-17) ", ["1916"]),
            ("Jeune Fille Assise 1919 ", ["1919"]),
            ("", []),
            ("Jeune Fille Assise (17th Century)", []),
            ("Jeune Fille Assise 1st Autumn Day 1518 (17th Century)", ["1518"])
        ]
        for case in testCases:
            actualMatches = artveeScraper.find_fourDigitNumbers(case[0])
            self.assertEqual(len(actualMatches), len(case[1]))
            for i in range(0, len(actualMatches)):
                self.assertEqual(actualMatches[i], case[1][i])

if __name__ == '__main__':
    unittest.main()