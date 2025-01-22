def num_to_words(num):

    up_to_19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    
    # Words for multiples of ten from 20 to 90
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    
    thousands = ['', 'Thousand', 'Million', 'Billion']

    def convert_chunk(n):
        if n == 0:
            return []
        elif n < 20:
            return [up_to_19[n]]
        elif n < 100:
            return [tens[n // 10]] + convert_chunk(n % 10)
        else:
            return [up_to_19[n // 100], 'Hundred'] + convert_chunk(n % 100)

    def convert_number(n):
        if n == 0:
            return 'Zero'
        
        words = []
        chunk_count = 0
        
        while n > 0:
            chunk = n % 1000
            if chunk > 0:
                words = convert_chunk(chunk) + [thousands[chunk_count]] + words
            n //= 1000
            chunk_count += 1
        
        return ' '.join(words).strip()

    return convert_number(num)


# Test cases
print(num_to_words(10754))  
print(num_to_words(19)) 
print(num_to_words(444))  
