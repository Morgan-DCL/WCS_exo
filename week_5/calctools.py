class CalcTools:
    """
    Une classe pour effectuer divers calculs mathématiques.

    Méthodes
    --------
    power_(n: float) -> float
        Returns le carré de n.

    cube_(n: float) -> float
        Returns le cube de n.

    abs_(n: float) -> float
        Returns la valeur absolue de n.

    factorial(n: float) -> float
        Returns le factoriel de n.

    sqrt_(n: float) -> float
        Returns la racine carrée de n.

    pow_(n: float, exponent: float) -> float
        Returns n à la puissance de l'exposant.

    mode_(n_list: list) -> Union[float, List[float]]
        Returns le mode de n_list. Si plusieurs modes existent, Returns une liste de modes.

    avg_(n_list: list) -> float
        Returns la moyenne de n_list.

    max_(n_list: list) -> float
        Returns le maximum de n_list.

    min_(n_list: list) -> float
        Returns le minimum de n_list.
    """

    def __init__(self):
        return None

    def power_(self, n: float) -> float:
        """
        Calcule et renvoie le carré d'un nombre.

        Parameters
        ----------
        n : float
            Le nombre à élever au carré.

        Returns
        -------
        float
            Le carré du nombre d'entrée.
        """
        return n**2

    def cube_(self, n: float) -> float:
        """
        Calcule le cube d'un nombre.

        Cette fonction prend un nombre en entrée et Returns son cube.
        Le nombre peut être un entier ou un flottant.

        Parameters
        ----------
        n : float
            Le nombre dont on veut calculer le cube.

        Returns
        -------
        float
            Le cube du nombre d'entrée.
        """
        return n**3

    def abs_(self, n: float) -> float:
        """
        Effectue une opération d'absolu sur un nombre flottant.

        Parameters
        ----------
        n : float
            Le nombre flottant sur lequel effectuer l'opération d'absolu.

        Returns
        -------
        float
            La valeur absolue du nombre flottant d'entrée.
            Si le nombre est négatif, il est converti en positif.
            Si le nombre est déjà positif ou zéro, il est renvoyé tel quel.
        """
        return -n if n < 0 else n

    def factorial(self, n: float) -> float:
        """
        Calcule le factoriel d'un nombre donné.

        Parameters
        ----------
        n : float
            Le nombre dont le factoriel doit être calculé. Doit être un nombre entier positif.

        Returns
        -------
        float
            Le factoriel du nombre donné. Si le nombre est 0, Returns 1.
        """
        if n == 0:
            return 1
        num = 1
        for i in range(1, n + 1):
            num *= i
        return num

    def sqrt_(self, n: float) -> float:
        """
        Calcule la racine carrée d'un nombre.

        Cette fonction prend un nombre en entrée et Returns sa racine carrée.
        Elle utilise l'opérateur d'exponentiation de Python (**) pour calculer la racine carrée.

        Parameters
        ----------
        n : float
            Le nombre dont on veut calculer la racine carrée.

        Returns
        -------
        float
            La racine carrée du nombre d'entrée
        """
        return n**0.5

    def pow_(self, n: float, exp: float) -> float:
        """
        Calcule la puissance d'un nombre.

        Cette fonction prend un nombre flottant et un exposant entier
        comme arguments et renvoie le nombre élevé à la puissance de l'exposant.
        Si l'exposant est égal à zéro, la fonction renvoie 1.
        Si l'exposant est négatif, la fonction inverse le nombre et
        rend l'exposant positif avant de calculer la puissance.

        Paramètres
        ----------
        n : float
            Le nombre à élever à une puissance.
        exp : int
            L'exposant auquel le nombre doit être élevé.

        Retourne
        -------
        float
            Le nombre 'n' élevé à la puissance 'exp'.

        """
        if exp == 0:
            return 1
        elif exp < 0:
            n, exp = 1 / n, -exp
        return n**exp

    def mode_(self, n_list: list):
        """
        Calcule le mode d'une liste de nombres.

        Cette fonction parcourt une liste de nombres et renvoie le mode de la liste.
        Si plusieurs modes sont présents, la fonction renvoie une liste de tous les modes.
        Si un seul mode est présent, la fonction renvoie ce mode.

        Parameters
        ----------
        n_list : list
            La liste de nombres pour laquelle le mode doit être calculé.

        Returns
        -------
        int or list
            Le mode de la liste si un seul mode est présent,
            sinon une liste de tous les modes.
        """

        countr = {}
        mode = 0
        for n in n_list:
            if n in countr:
                countr[n] += 1
            else:
                countr[n] = 1
        for k, v in countr.items():
            if v > mode:
                mode = v
        modes = [k for k, v, in countr.items() if v == mode]

        return modes[0] if len(modes) == 1 else modes

    def avg_(self, n_list) -> float:
        """
        Calcule la moyenne des nombres dans une liste donnée.

        Parameters
        ----------
        n_list : list
            Une liste de nombres (int, float) dont la moyenne doit être calculée.

        Returns
        -------
        float
            La moyenne arrondie à deux chiffres après la virgule des nombres dans la liste donnée.
        """

        return round(sum([n for n in n_list]) / len(n_list), 2)

    def max_(self, n_list: list):
        """
        Effectue une fonction qui trouve et Returns le nombre maximum dans une liste donnée.

        Parameters
        ----------
            Une liste de nombres entiers ou flottants.

        Returns
        -------
        num : int ou float
            Le nombre maximum trouvé dans la liste donnée.
        """
        max_ = n_list[0]
        for n in n_list:
            if n > max_:
                max_ = n
        return max_

    def min_(self, n_list: list):
        """
        Effectue une fonction qui trouve et Returns le nombre minimum dans une liste donnée.

        Parameters
        ----------
        n_list : list
            Une liste de nombres entiers ou réels.

        Returns
        -------
        num : int ou float
            Le nombre minimum trouvé dans la liste donnée.
        """
        min_ = n_list[0]
        for n in n_list:
            if n < min_:
                min_ = n
        return min_