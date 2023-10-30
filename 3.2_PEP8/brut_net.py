import json
import numpy as np


file_impot = "taux_imposition.json"

class BrutNet():
    """
    Class BrutNet
    ----------------

    A class to calculate the net salary after considering
    different taxations and commissions.

    Attributes:
    ----------
    salaire : float
        The initial gross salary.

    commission : float, optional (default=0.1)
        The percentage of commission given as a
        fraction of the salary (e.g., 0.1 for 10%).

    taxe_cadre : float, optional (default=0.25)
        The percentage of the cadre tax deducted as a
        fraction of the salary with commission (e.g., 0.25 for 25%).

    taux_impot : dict
        A dictionary that maps salary ranges to their
        respective tax percentages. Loaded from "taux_imposition.json".

    Methods:
    -------
    get_import_pct():
        Returns the tax percentage corresponding to the
        current salary based on taux_impot.

    calc_commision():
        Calculates and returns the commission value for
        the given salary.

    calc_salaire_with_commission():
        Calculates and returns the gross salary
        including the commission.

    calc_after_taxe_cadre():
        Calculates and returns the salary after
        deducting the cadre tax.

    calc_after_impot():
        Calculates and returns the salary after
        deducting the income tax.

    calc_net_salary():
        Calculates and returns the net salary
        after all deductions.
    """

    def __init__(
        self, salaire, commission=0.1, taxe_cadre=0.25
    ):
        """
        Initializes the BrutNet object with the given parameters.

        Parameters:
        ----------
        salaire : float
            The initial gross salary.
        commission : float, optional (default=0.1)
            The commission rate to be applied on the salary.
        taxe_cadre : float, optional (default=0.25)
            The cadre tax rate to be applied on the salary with commission.
        """

        self.salaire = salaire
        self.commission = commission
        self.taxe_cadre = taxe_cadre

        with open(file_impot, "r") as fp:
            taux_impot_str = json.load(fp)

        self.taux_impot = {
            (int(lower), np.inf if upper == "inf" else int(upper)): v
            for k, v in taux_impot_str.items()
            for lower, upper in [k.split("-")]
        }

    def get_import_pct(self):
        """
        Retrieves the tax percentage corresponding to the current
        salary from the taux_impot attribute.

        Returns:
        -------
        float
            The tax percentage as a fraction (e.g., 0.2 for 20%).
        """

        for i, impot_pct in self.taux_impot.items():
            if i[0] <= self.salaire < i[1]:
                return impot_pct

    def calc_commision(self):
        """
        Calculates the commission based on the initial gross salary.

        Returns:
        -------
        float
            The calculated commission value.
        """

        commission_value = self.salaire * self.commission
        return commission_value

    def calc_salaire_with_commission(self):
        """
        Calculates the salary after adding the commission.

        Returns:
        -------
        float
            The salary inclusive of the commission.
        """

        return self.salaire + self.calc_commision()

    def calc_after_impot(self):
        """
        Calculates the salary after the deduction of the cadre tax.

        Returns:
        -------
        float
            Salary value after the cadre tax deduction.
        """

        net_avant_impostion = (
            self.calc_after_taxe_cadre() * (1 - self.get_import_pct())
        )
        return net_avant_impostion

    def calc_after_taxe_cadre(self):
        """
        Calculates the salary after the deduction of the
        applicable income tax.

        Returns:
        -------
        float
            Salary value after the income tax deduction.
        """

        taxe_cadre_value = (
            self.calc_salaire_with_commission() * (1 - self.taxe_cadre)
        )
        return taxe_cadre_value

    def calc_net_salary(self):
        """
        Computes the net salary considering all deductions and commissions.

        Returns:
        -------
        float
            The final net salary after all deductions.
        """

        net_salary = self.calc_after_impot()
        return net_salary


salaire_brut = 5500

net = BrutNet(salaire_brut, commission=0)

print(f"Montant de la commision :\n{net.calc_commision()}")
print(
    f"Total salaire et commision :\n{net.calc_salaire_with_commission()}")
print(
    f"Total salaire net :\n{net.calc_after_taxe_cadre()}")
print(
    f"Taux d'imposition :\n{round(net.get_import_pct() * 100, 2)} %")
print(
    f"Salaire net après impot :\n{round(net.calc_net_salary(), 2)}")
