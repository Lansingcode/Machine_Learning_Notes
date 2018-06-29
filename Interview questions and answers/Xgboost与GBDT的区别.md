1. 算法层面Xgboost加了正则项，普通GBDT没有  
正则项可以防止过拟合  
$$J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha}$$
