(define (evenSub s)
  (if (null? s) nil
    (append (evenSub (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (even? (car s))
          (evenSub (cdr s))
          (oddSub (cdr s))
          )
        )
      (if (even? (car s)) (list (list (car s))) nil))))

(define (oddSub s)
  (if (null? s) nil
    (append (oddSub (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (odd? (car s))
          (evenSub (cdr s))
          (oddSub (cdr s))))
      (if 
      (odd? (car s)) 
      (list (list (car s)))
      nil)))
      )
      

