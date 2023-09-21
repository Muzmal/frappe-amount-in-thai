from num2words import num2words
import frappe

@frappe.whitelist()
def amount_in_thai( amount ):
    if( amount > 0 ):
        return num2words(amount, to = 'currency',lang="th")
    else:
        return "Missing amount"