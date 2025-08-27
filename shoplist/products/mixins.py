from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SalesExecutiveRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_sales_executive or self.request.user.is_admin
