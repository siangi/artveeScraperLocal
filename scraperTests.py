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
            actualMatches = artveeScraper.findFourDigitNumbers(case[0])
            self.assertEqual(len(actualMatches), len(case[1]))
            for i in range(0, len(actualMatches)):
                self.assertEqual(actualMatches[i], case[1][i])

    def test_twoDigitCentury(self):
        testCases = [
            ("Pubertet (1937) ", []),
            ("44. Plafond du Tombeau Dâ€™amenemant (nÂ° 58) (1911)", []),
            ("Ontwerp voor raam in het Noordertransept in de Dom te Utrecht 5 (ca. 1878-1938)", []),
            ("Tak met jonge loten (1874) ", []),
            ("Tak met jonge loten (19th Century) ", ["19"]),
            ("19th Regiment, 17th Century", ["17"]),
            ("16th Century Paris (18th Century) ", ["16","18"])   
        ]

        for case in testCases:
            actualMatches = artveeScraper.findCenturyNumbers(case[0])
            self.assertEqual(len(actualMatches), len(case[1]))
            for i in range(0, len(actualMatches)):
                self.assertEqual(actualMatches[i], case[1][i])

    def test_findYear(self):
        testCases = [
            ("Pubertet (1937) ", (1937, False)),
            ("Ontwerp voor raam in het Noordertransept in de Dom te Utrecht 5 (ca. 1878-1938)", (1938, False)),
            ("Tak met jonge loten (19th Century) ", (1800, True)),
            ("19th Regiment, 17th Century", (1600, True)),
            ("16th Century Paris (18th Century) ", (1700, True)),
            ("19th Century Paris (1802)", (1802, False)),
            ("", (-1, False)),
            ("Guernica", (-1, False))
        ]

        for case in testCases:
            actualResult = artveeScraper.findYear(case[0])
            self.assertEqual(actualResult[0], case[1][0])
            self.assertEqual(actualResult[1], case[1][1])

if __name__ == '__main__':
    unittest.main()