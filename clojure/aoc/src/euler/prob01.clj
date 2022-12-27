(ns euler.prob01)

(->> (range 1000)
     (filter #(or (= 0 (mod % 3)) (= 0 (mod % 5))))
     (reduce +))