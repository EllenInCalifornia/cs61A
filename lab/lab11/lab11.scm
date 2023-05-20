(define (over-or-under num1 num2)
  (cond ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1)
    ))

(define (make-adder num) (lambda (inc) (+ num inc) ))

(define (composed f g)
  (lambda (x) (f (g x)))
  )

(define (repeat f n)
  (if (< n 1) (lambda (x) x)
              (composed f (repeat f (- n 1)))
    )

  )

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (cond
    ((zero? a) b)
    ((zero? b) a)
    (
      (zero? (modulo (max a b)(min a b))) (min a b)
      )
    (else (gcd (min a b)(modulo (max a b)(min a b))))
    )
  )
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
                    (if (even? (car s))
                      (oddSub (cdr s))
                      (evenSub (cdr s))))
                  (if (odd? (car s)) (list(list((car s))) nil)))))