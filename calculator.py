import math


class GearCalculator:
    """
    Helical Gear Over Pin Measurement Calculator

    Calculates:
    - Ideal Pin Diameter
    - Measure Over Pin using Manual Pin
    - Measure Over Pin using Ideal Pin
    """

    def __init__(
        self,
        module,
        teeth,
        pressure_angle,
        beta_degree,
        beta_minute,
        beta_second,
        profile_shift,
        manual_pin
    ):

        self.m = module
        self.z = teeth
        self.alpha = pressure_angle

        self.beta_degree = beta_degree
        self.beta_minute = beta_minute
        self.beta_second = beta_second

        self.xfactor = profile_shift
        self.manual_pin = manual_pin


    def calculate(self):

        # -----------------------------
        # Initial conversion
        # -----------------------------

        alpha_R = math.radians(self.alpha)

        beta0 = (
            self.beta_degree
            + self.beta_minute / 60
            + self.beta_second / 3600
        )

        beta_R = math.radians(beta0)


        # -----------------------------
        # Equivalent spur gear
        # -----------------------------

        zv = self.z / (math.cos(beta_R) ** 3)


        inv_alpha = (
            math.tan(alpha_R)
            - alpha_R
        )


        # Space width half angle

        muv = (
            math.pi / (2*zv)
            - inv_alpha
            - (
                2*self.xfactor
                * math.tan(alpha_R)
                / zv
            )
        )


        # -----------------------------
        # Ideal pin diameter
        # -----------------------------

        alpha_prim_v = math.degrees(
            math.acos(
                (
                    zv *
                    math.cos(alpha_R)
                )
                /
                (
                    zv
                    + 2*self.xfactor
                )
            )
        )


        alpha_prim_v_R = math.radians(alpha_prim_v)


        phi_v = (
            math.tan(alpha_prim_v_R)
            +
            muv
        )


        inv_phiv = (
            math.tan(phi_v)
            -
            phi_v
        )


        ideal_pin = (
            zv
            * self.m
            * math.cos(alpha_R)
            *
            (
                inv_phiv
                +
                muv
            )
        )


        # -----------------------------
        # Function for MOP calculation
        # -----------------------------

        def calculate_mop(dp):

            alpha_t = math.degrees(
                math.atan(
                    math.tan(alpha_R)
                    /
                    math.cos(beta_R)
                )
            )


            alpha_tR = math.radians(alpha_t)


            inv_alpha_t = (
                math.tan(alpha_tR)
                -
                alpha_tR
            )


            inv_phi = (
                dp
                /
                (
                    self.m
                    *
                    self.z
                    *
                    math.cos(alpha_R)
                )
                -
                math.pi/(2*self.z)
                +
                inv_alpha_t
                +
                (
                    2*self.xfactor
                    *
                    math.tan(alpha_R)
                    /
                    self.z
                )
            )


            # Newton Raphson

            phi = math.radians(30)

            tolerance = 1e-12

            max_iteration = 100


            for i in range(max_iteration):

                f = (
                    math.tan(phi)
                    -
                    phi
                    -
                    inv_phi
                )


                df = (
                    math.tan(phi)**2
                )


                phi_new = (
                    phi
                    -
                    f/df
                )


                if abs(phi_new - phi) < tolerance:
                    phi = phi_new
                    break


                phi = phi_new



            mop = (
                self.z
                *
                self.m
                *
                math.cos(alpha_tR)
                /
                (
                    math.cos(beta_R)
                    *
                    math.cos(phi)
                )
                +
                dp
            )


            return mop



        # -----------------------------
        # Two measurements
        # -----------------------------

        mop_manual = calculate_mop(
            self.manual_pin
        )


        mop_ideal = calculate_mop(
            ideal_pin
        )


        return {

            "Ideal Pin Diameter": round(
                ideal_pin,
                8
            ),

            "MOP Manual Pin": round(
                mop_manual,
                6
            ),

            "MOP Ideal Pin": round(
                mop_ideal,
                6
            )
        }