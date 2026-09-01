class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """Add a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, other_category):
        """Transfer an amount to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        """Check if sufficient funds exist for a transaction."""
        return self.get_balance() >= amount
    
    def __str__(self):
        """Return a string representation of the category."""
        # Create title line (30 characters total)
        title = self.name.center(30, "*")
        lines = [title]
        
        # Add ledger items
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:>7.2f}"
            lines.append(f"{description}{amount}")
        
        # Add total line
        total = self.get_balance()
        lines.append(f"Total: {total:.2f}")
        
        return "\n".join(lines)


def create_spend_chart(categories):
    """Create a bar chart showing percentage spent by category."""
    # Calculate total amount spent (only withdrawals)
    total_spent = 0
    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += abs(item["amount"])
    
    # Calculate percentage spent for each category
    percentages = {}
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        
        if total_spent == 0:
            percentage = 0
        else:
            percentage = (spent / total_spent) * 100
        
        # Round down to nearest 10
        percentages[category.name] = int(percentage // 10) * 10
    
    # Build the chart
    lines = ["Percentage spent by category"]
    
    # Add percentage lines (from 100 down to 0)
    for percent in range(100, -1, -10):
        line = f"{percent:>3}|"
        for i, category in enumerate(categories):
            if percentages[category.name] >= percent:
                line += " o"
            else:
                line += "  "
            # Add spacing: 1 space between categories, 2 spaces after last
            if i < len(categories) - 1:
                line += " "
            else:
                line += "  "
        lines.append(line)
    
    # Add horizontal line (3 dashes per category + 2 extra)
    dashes = "-" * (len(categories) * 3 + 2)
    lines.append("    " + dashes)
    
    # Add category names vertically
    max_name_length = max(len(category.name) for category in categories)
    
    for i in range(max_name_length):
        line = "    "
        for j, category in enumerate(categories):
            line += " "  # Leading space to align with bar spacing
            if i < len(category.name):
                line += category.name[i]
            else:
                line += " "
            # Add spacing: 1 space between categories, 2 spaces after last
            if j < len(categories) - 1:
                line += " "
            else:
                line += "  "
        lines.append(line)
    
    return "\n".join(lines)
