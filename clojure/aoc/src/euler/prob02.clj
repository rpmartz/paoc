(ns euler.prob02)

(defn fib [n]
  (case n
    0 0
    1 1
    (+ (fib (- n 1)) (fib (- n 2)))))


(reduce + (filter even? (take-while #(< % 4000000) (map fib (range)))))