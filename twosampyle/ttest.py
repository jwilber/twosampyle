from scipy.stats import t

class TTest():
    
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        
    @staticmethod
    def t_statistic(a,b):
        """"""
        N_a = len(a)
        N_b = len(b)
        mu_a = np.mean(a)
        mu_b = np.mean(b)
        var_a = np.var(a, ddof=1) # make denominator N-1: unbiased estimate of var
        var_b = np.var(b, ddof=1)
        s_a = np.sqrt(var_a)
        s_b = np.sqrt(var_b)
        
        # Equal Variance
        if var_a == var_b:
            t_num = mu_a - mu_b
            # t_denom = np.sqrt(2. / N_a) * np.sqrt( (var_a + var_b) / 2 )
            t_denom = np.sqrt( 1.*((N_a-1)*var_a + (N_b-1)*var_b) / (N_a + N_b - 2) ) * np.sqrt( 1./N_a + 1./N_b )
            t_stat = 1. * t_num / t_denom
            return t_stat
        
        # unequal variance
        else:
            t_num = mu_a - mu_b
            t_denom = np.sqrt( 1. * var_a / N_a + 1. * var_b / N_b)
            t_stat = 1. * t_num / t_denom
            return t_stat

        
    def testStat(self, input_a=None, input_b=None):
        """"""
        if input_a or input_b:
            ttest_stat = TTest.t_statistic(input_a, input_b)
        else:
            ttest_stat = TTest.t_statistic(self.a, self.b)
        return ttest_stat
    
    
    def pvalue(self, input_a=None, input_b=None, sided='one'):
        """"""
        if input_a:
            N = len(input_a)
        else:
            N = len(self.a)
            
        # degrees of freedom
        df = 2*N - 2
        # test-statistic
        test_statistic = self.testStat(input_a, input_b)
        
        # p-value 
        p = 1 - t.cdf(np.abs(test_statistic), df=df) 
        
#         if sided != 'one' or sided != 'two':
#             raise ValueError("sided must be either 'one' or 'two'")
        if sided == 'one':
            p_value = p
        else: # two-sided
            p_value = 2*p
            
        return p_value
    
    
    def plot_dsn(self, input_a = None, input_b = None):
        """"""
        if input_a:
            N = len(input_a)
        else:
            N = len(self.a)
        df = 2*N - 2
        
        test_stat = self.testStat(input_a, input_b)
        fig, ax = plt.subplots(1, 1)
        x = np.linspace(t.ppf(0.01, df), 
                        t.ppf(0.99, df), 100)
        ax.plot(x, t.pdf(x, df), 
                'r-', lw=5, alpha=0.6, label='t pdf')
        ax.set_xlabel('Test Statistic Values')
        ax.set_ylabel('Probability')
        ax.set_title('T-Distribution with {}. D.o.F.'.format(df))
        plt.axvline(test_stat, lw=7)
        plt.show()

